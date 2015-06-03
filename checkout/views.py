from django.contrib import messages
from django import http
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from paypal.payflow.facade import authorize, sale

from oscar.apps.checkout import views, exceptions, signals
from oscar.apps.payment.forms import BankcardForm
from oscar.apps.payment.models import SourceType
from oscar.apps.order.models import BillingAddress

from django.utils import six
from django.conf import settings

#from paypal.pro.helpers import PayPalWPP

from .forms import BillingAddressForm, PaymentForm

from paypal.standard.forms import PayPalPaymentsForm

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
            ctx['bankcard_form'] = BankcardForm()
        if 'paypal_form' not in kwargs:
            ctx['paypal_form'] = PayPalPaymentsForm()
        return ctx




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
        #post=request.POST
        submission = self.build_submission()
        print 'en el handle_payment_details_submission'
        print submission['order_total']
        order_number = self.generate_order_number(submission['basket'])
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": submission['order_total'].excl_tax,
            "item_name": "Tequila",
            "invoice": order_number,
            "currency_code": submission['order_total'].currency,
            #"notify_url": "http://www.example.com",# + reverse('paypal-ipn'),
            "return_url": "http://maravatio.haushaus.mx/checkout/preview/",
            "cancel_return": "http://maravatio.haushaus.mx/checkout/preview/",
        }
        paypal_form = PayPalPaymentsForm(initial=paypal_dict)
        # bc_args = {
        #     'number': post['acct'],
        #     'expiry_month_0': post['expdate_0'],
        #     'expiry_month_1': post['expdate_1'],
        #     'ccv': post['cvv2']
        # }
        # print 'bc_args'
        # print bc_args
        # print 'post'
        # print post
        # #print bc_args
        # #number=post['acct']
        # #expiry_month_0 = post['expdate_0']
        # #expiry_month_1 = post['expdate_1']
        # #ccv = post['ccv2']
        # bankcard_form = BankcardForm(bc_args)
        # print 'valid bcform?'
        # print bankcard_form.is_valid()
        #print bankcard_form.backard
        #shipping_address = self.get_shipping_address(
        #    self.request.basket)
        #address_form = BillingAddressForm(shipping_address, request.POST)
        #print address_form.is_valid()
        #print request.POST
        #print bankcard_form.is_valid()

        #if paypal_form.is_valid(): #and bankcard_form.is_valid(): #address_form.is_valid() and bankcard_form.is_valid():
            # If both forms are valid, we render the preview view with the
            # forms hidden within the page. This seems odd but means we don't
            # have to store sensitive details on the server.
        return self.render_preview(request, paypal_form=paypal_form)#, bankcard_form=bankcard_form)#, billing_address_form=address_form)

        # Forms are invalid - show them to the customer along with the
        # validation errors.
        #return self.render_payment_details(request, paypal_form=paypal_form)#, bankcard_form=bankcard_form)#,billing_address_form=address_form)

    def handle_place_order_submission(self, request):
        #paypal_form = PaymentForm(request.POST)
        #bankcard_form = BankcardForm(request.POST)
        #shipping_address = self.get_shipping_address(
        #    self.request.basket)
        #print request.POST
        #address_form = BillingAddressForm(shipping_address, request.POST)
        #print 'handling order submision'
        #print address_form.is_valid()
        #print address_form.__dict__

        #a = bankcard_form.is_valid()
        #print a
        # if paypal_form.is_valid() and bankcard_form.is_valid(): #address_form.is_valid() and bankcard_form.is_valid():
        #     # Forms still valid, let's submit an order
        #     submission = self.build_submission(
        #         #order_kwargs={
        #         #    'billing_address': address_form.save(commit=False),
        #         #},
        #         payment_kwargs={
        #             'bankcard_form': bankcard_form,
        #             'paypal_form': paypal_form,
        #             #'billing_address_form': address_form
        #         }
        #     )
        #     print 'about to submit'
        #     return self.submit(**submission)
        return self.submit(**self.build_submission())
        # Must be DOM tampering as these forms were valid and were rendered in
        # a hidden element.  Hence, we don't need to be that friendly with our
        # error message.
        # print 'invalid submision'
        # messages.error(request, _("Invalid submission"))
        # return http.HttpResponseRedirect(
        #     reverse('checkout:payment-details'))


    def submit(self, user, basket, shipping_address, shipping_method,  # noqa (too complex (10))
               shipping_charge, billing_address, order_total,
               payment_kwargs=None, order_kwargs=None):
        """
        Submit a basket for order placement.

        The process runs as follows:

         * Generate an order number
         * Freeze the basket so it cannot be modified any more (important when
           redirecting the user to another site for payment as it prevents the
           basket being manipulated during the payment process).
         * Attempt to take payment for the order
           - If payment is successful, place the order
           - If a redirect is required (eg PayPal, 3DSecure), redirect
           - If payment is unsuccessful, show an appropriate error message

        :basket: The basket to submit.
        :payment_kwargs: Additional kwargs to pass to the handle_payment
                         method. It normally makes sense to pass form
                         instances (rather than model instances) so that the
                         forms can be re-rendered correctly if payment fails.
        :order_kwargs: Additional kwargs to pass to the place_order method
        """
        if payment_kwargs is None:
            payment_kwargs = {}
        if order_kwargs is None:
            order_kwargs = {}

        # Taxes must be known at this point
        assert basket.is_tax_known, (
            "Basket tax must be set before a user can place an order")
        assert shipping_charge.is_tax_known, (
            "Shipping charge tax must be set before a user can place an order")

        # We generate the order number first as this will be used
        # in payment requests (ie before the order model has been
        # created).  We also save it in the session for multi-stage
        # checkouts (eg where we redirect to a 3rd party site and place
        # the order on a different request).
        order_number = self.generate_order_number(basket)
        self.checkout_session.set_order_number(order_number)
        views.logger.info("Order #%s: beginning submission process for basket #%d",
                    order_number, basket.id)

        # Freeze the basket so it cannot be manipulated while the customer is
        # completing payment on a 3rd party site.  Also, store a reference to
        # the basket in the session so that we know which basket to thaw if we
        # get an unsuccessful payment response when redirecting to a 3rd party
        # site.
        self.freeze_basket(basket)
        self.checkout_session.set_submitted_basket(basket)

        # We define a general error message for when an unanticipated payment
        # error occurs.
        error_msg = _("A problem occurred while processing payment for this "
                      "order - no payment has been taken.  Please "
                      "contact customer services if this problem persists")

        signals.pre_payment.send_robust(sender=self, view=self)
        print 'en submit'
        try:
            print 'en try handle'
            print order_number
            self.handle_payment(order_number, order_total, **payment_kwargs)
        except views.RedirectRequired as e:
            # Redirect required (eg PayPal, 3DS)
            views.logger.info("Order #%s: redirecting to %s", order_number, e.url)
            return http.HttpResponseRedirect(e.url)
        except views.UnableToTakePayment as e:
            # Something went wrong with payment but in an anticipated way.  Eg
            # their bankcard has expired, wrong card number - that kind of
            # thing. This type of exception is supposed to set a friendly error
            # message that makes sense to the customer.
            msg = six.text_type(e)
            views.logger.warning(
                "Order #%s: unable to take payment (%s) - restoring basket",
                order_number, msg)
            self.restore_frozen_basket()

            # We assume that the details submitted on the payment details view
            # were invalid (eg expired bankcard).
            return self.render_payment_details(
                self.request, error=msg, **payment_kwargs)
        except views.PaymentError as e:
            # A general payment error - Something went wrong which wasn't
            # anticipated.  Eg, the payment gateway is down (it happens), your
            # credentials are wrong - that king of thing.
            # It makes sense to configure the checkout logger to
            # mail admins on an error as this issue warrants some further
            # investigation.
            msg = six.text_type(e)
            views.logger.error("Order #%s: payment error (%s)", order_number, msg,
                         exc_info=True)
            self.restore_frozen_basket()
            return self.render_preview(
                self.request, error=error_msg, **payment_kwargs)
        except Exception as e:
            # Unhandled exception - hopefully, you will only ever see this in
            # development...
            views.logger.error(
                "Order #%s: unhandled exception while taking payment (%s)",
                order_number, e, exc_info=True)
            self.restore_frozen_basket()
            return self.render_preview(
                self.request, error=error_msg, **payment_kwargs)

        signals.post_payment.send_robust(sender=self, view=self)

        # If all is ok with payment, try and place order
        views.logger.info("Order #%s: payment successful, placing order",
                    order_number)
        try:
            return self.handle_order_placement(
                order_number, user, basket, shipping_address, shipping_method,
                shipping_charge, billing_address, order_total, **order_kwargs)
        except views.UnableToPlaceOrder as e:
            # It's possible that something will go wrong while trying to
            # actually place an order.  Not a good situation to be in as a
            # payment transaction may already have taken place, but needs
            # to be handled gracefully.
            msg = six.text_type(e)
            views.logger.error("Order #%s: unable to place order - %s",
                         order_number, msg, exc_info=True)
            self.restore_frozen_basket()
            return self.render_preview(
                self.request, error=msg, **payment_kwargs)


    def handle_payment(self, order_number, total, **kwargs):
        # Make request to PayPal - if there any problems (eg bankcard
        # not valid / request refused by bank) then an exception would be
        # raised and handled by the parent PaymentDetail view)
        #facade = Facade()
        print 'hndle peyment'
        #print kwargs['bankcard_form']['acct'].value()
        item = {
            'invnum': order_number,
            'amt': total.incl_tax
        }
        #success = kwargs['paypal_form'].process(self.request, item)
        #print success
        #print bankcard
        #order_number, paypal, amt=total.incl_tax
        #paypalwpp = PayPalWPP()

        #print 'en el handle payment'
        paypal_ref ='000test'
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
