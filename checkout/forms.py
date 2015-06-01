from django import forms

from oscar.apps.payment import forms as payment_forms
from oscar.apps.order.models import BillingAddress

from paypal.pro.fields import CreditCardField, CreditCardExpiryField, CreditCardCVV2Field, CountryField
from paypal.pro.exceptions import PayPalFailure


class PaymentForm(forms.Form):
    """Form used to process direct payments."""
    firstname = forms.CharField(255, label="First Name")
    lastname = forms.CharField(255, label="Last Name")
    street = forms.CharField(255, label="Street Address")
    city = forms.CharField(255, label="City")
    state = forms.CharField(255, label="State")
    countrycode = CountryField(label="Country", initial="US")
    zip = forms.CharField(32, label="Postal / Zip Code")
    acct = CreditCardField(label="Credit Card Number")
    expdate = CreditCardExpiryField(label="Expiration Date")
    cvv2 = CreditCardCVV2Field(label="Card Security Code")
    currencycode = forms.CharField(widget=forms.HiddenInput(), initial="MXN")

    def process(self, request, item):
        """Process a PayPal direct payment."""
        from paypal.pro.helpers import PayPalWPP
        print 'in process'
        wpp = PayPalWPP(request)
        params = self.cleaned_data
        params['creditcardtype'] = self.fields['acct'].card_type
        params['expdate'] = self.cleaned_data['expdate'].strftime("%m%Y")
        params['ipaddress'] = request.META.get("REMOTE_ADDR", "")
        params.update(item)

        try:
            # Create single payment:
            if 'billingperiod' not in params:
                print 'before dodirectpayment'
                nvp_obj = wpp.doDirectPayment(params)
                #print nvp_obj
            # Create recurring payment:
            else:
                nvp_obj = wpp.createRecurringPaymentsProfile(params, direct=True)
        except PayPalFailure:
            return False
        return True


class ConfirmForm(forms.Form):
    """Hidden form used by ExpressPay flow to keep track of payer information."""
    token = forms.CharField(max_length=255, widget=forms.HiddenInput())
    PayerID = forms.CharField(max_length=255, widget=forms.HiddenInput())



class BillingAddressForm(payment_forms.BillingAddressForm):
    """
    Extended version of the core billing address form that adds a field so
    customers can choose to re-use their shipping address.
    """
    SAME_AS_SHIPPING, NEW_ADDRESS = 'same', 'new'
    CHOICES = (
        (SAME_AS_SHIPPING, 'Use shipping address'),
        (NEW_ADDRESS, 'Enter a new address'),
    )
    same_as_shipping = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES, initial=SAME_AS_SHIPPING)
    class Meta(payment_forms.BillingAddressForm):
        model = BillingAddress
        exclude = ('search_text', 'first_name', 'last_name')
    def __init__(self, shipping_address, data=None, *args, **kwargs):
        # Store a reference to the shipping address
        self.shipping_address = shipping_address
        super(BillingAddressForm, self).__init__(data, *args, **kwargs)
        # If no shipping address (eg a download), then force the
        # 'same_as_shipping' field to have a certain value.
        if shipping_address is None:
            self.fields['same_as_shipping'].choices = (
                (self.NEW_ADDRESS, 'Enter a new address'),)
            self.fields['same_as_shipping'].initial = self.NEW_ADDRESS
        # If using same address as shipping, we don't need require any of the
        # required billing address fields.
        if data and data.get('same_as_shipping', None) == self.SAME_AS_SHIPPING:
            for field in self.fields:
                if field != 'same_as_shipping':
                    self.fields[field].required = False
    def _post_clean(self):
        # Don't run model validation if using shipping address
        if self.cleaned_data.get('same_as_shipping') == self.SAME_AS_SHIPPING:
            return
        super(BillingAddressForm, self)._post_clean()
    def save(self, commit=True):
        if self.cleaned_data.get('same_as_shipping') == self.SAME_AS_SHIPPING:
            # Convert shipping address into billing address
            billing_addr = BillingAddress()
            self.shipping_address.populate_alternative_model(billing_addr)
            if commit:
                billing_addr.save()
            return billing_addr
        return super(BillingAddressForm, self).save(commit)