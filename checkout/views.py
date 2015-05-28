from django.contrib import messages
from django import http
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from paypal.payflow.facade import authorize, sale

from oscar.apps.checkout import views, exceptions
from oscar.apps.payment.forms import BankcardForm
from oscar.apps.payment.models import SourceType
from oscar.apps.order.models import BillingAddress

from paypal.pro.forms import PaymentForm

from .forms import BillingAddressForm


# Customise the core PaymentDetailsView to integrate Datacash
class PaymentDetailsView(views.PaymentDetailsView):

    def check_payment_data_is_captured(self, request):
        if request.method != "POST":
            raise exceptions.FailedPreCondition(
                url=reverse('checkout:payment-details'),
                message=_("Please enter your payment details"))

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        # Ensure newly instantiated instances of the bankcard and billing
        # address forms are passed to the template context (when they aren't
        # already specified).
        if 'bankcard_form' not in kwargs:
            ctx['bankcard_form'] = PaymentForm()
        if 'billing_address_form' not in kwargs:
            ctx['billing_address_form'] = self.get_billing_address_form(
                ctx['shipping_address']
            )
        elif kwargs['billing_address_form'].is_valid():
            # On the preview view, we extract the billing address into the
            # template context so we can show it to the customer.
            ctx['billing_address'] = kwargs[
                'billing_address_form'].save(commit=False)
        #print ctx
        return ctx


    def get_billing_address_form(self, shipping_address):
        """
        Return an instantiated billing address form
        """
        addr = self.get_default_billing_address()
        if not addr:
            return BillingAddressForm(shipping_address=shipping_address)
        billing_addr = BillingAddress()
        addr.populate_alternative_model(billing_addr)
        return BillingAddressForm(shipping_address=shipping_address,
                                  instance=billing_addr)

    def post(self, request, *args, **kwargs):
        # Posting to payment-details isn't the right thing to do.  Form
        # submissions should use the preview URL.
        if not self.preview:
            return http.HttpResponseBadRequest()

        # We use a custom parameter to indicate if this is an attempt to place
        # an order (normally from the preview page).  Without this, we assume a
        # payment form is being submitted from the payment details view. In
        # this case, the form needs validating and the order preview shown.
        if request.POST.get('action', '') == 'place_order':
            #print 'place order'
            #print request.POST
            return self.handle_place_order_submission(request)
        #print 'submitting'
        return self.handle_payment_details_submission(request)


    def handle_payment_details_submission(self, request):
        # Validate the submitted forms
        bankcard_form = PaymentForm(request.POST)
        shipping_address = self.get_shipping_address(
            self.request.basket)
        address_form = BillingAddressForm(shipping_address, request.POST)
        #print address_form.is_valid()
        #print bankcard_form.is_valid()

        if address_form.is_valid() and bankcard_form.is_valid():
            # If both forms are valid, we render the preview view with the
            # forms hidden within the page. This seems odd but means we don't
            # have to store sensitive details on the server.
            return self.render_preview(
                request, bankcard_form=bankcard_form,
                billing_address_form=address_form)

        # Forms are invalid - show them to the customer along with the
        # validation errors.
        return self.render_payment_details(
            request, bankcard_form=bankcard_form,
            billing_address_form=address_form)

    def handle_place_order_submission(self, request):
        bankcard_form = PaymentForm(request.POST)
        shipping_address = self.get_shipping_address(
            self.request.basket)
        #print request.POST
        address_form = BillingAddressForm(shipping_address, request.POST)
        #print 'handling order submision'
        #print address_form.is_valid()
        #print address_form.__dict__

        #a = bankcard_form.is_valid()
        #print a
        if address_form.is_valid() and bankcard_form.is_valid():
            # Forms still valid, let's submit an order
            submission = self.build_submission(
                order_kwargs={
                    'billing_address': address_form.save(commit=False),
                },
                payment_kwargs={
                    'bankcard_form': bankcard_form,
                    'billing_address_form': address_form
                }
            )
            print 'about to submit'
            return self.submit(**submission)
        # Must be DOM tampering as these forms were valid and were rendered in
        # a hidden element.  Hence, we don't need to be that friendly with our
        # error message.
        print 'invalid submision'
        messages.error(request, _("Invalid submission"))
        return http.HttpResponseRedirect(
            reverse('checkout:payment-details'))




    def handle_payment(self, order_number, total, **kwargs):
        # Make request to PayPal - if there any problems (eg bankcard
        # not valid / request refused by bank) then an exception would be
        # raised and handled by the parent PaymentDetail view)
        #facade = Facade()
        bankcard = kwargs['bankcard_form'].bankcard
        ##
        paypal_ref = authorize(
            order_number, total.incl_tax, bankcard)
        print 'en el handle payment'
        # Request was successful - record the "payment source".  As this
        # request was a 'pre-auth', we set the 'amount_allocated' - if we had
        # performed an 'auth' request, then we would set 'amount_debited'.
        source_type, _ = SourceType.objects.get_or_create(name='PayPal')
        source = source_type.sources.model(
            source_type=source_type,
            currency=total.currency,
            amount_allocated=total.incl_tax,
            reference=paypal_ref)
        print source
        self.add_payment_source(source)

        # Also record payment event
        self.add_payment_event(
            'pre-auth', total.incl_tax, reference=paypal_ref)
