from django.shortcuts import render
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView


class PaymentDetailsView(CorePaymentDetailsView):
    template_name = 'checkout/payment_det.html'
    template_name_preview = 'checkout/prev.html'

# Create your views here.
