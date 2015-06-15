from oscar.apps.basket.views import BasketAddView as CoreBasketAddView

from django.core.urlresolvers import reverse

from django import shortcuts

from django.utils.http import is_safe_url

from django.dispatch.dispatcher import receiver
from oscar.apps.basket.signals import basket_addition

from oscar.core.utils import safe_referrer

from django.contrib import messages
#from django.shortcuts import redirect
from django.template.loader import render_to_string


# def get_messages(basket, offers_before, offers_after,
#                  include_buttons=True):
#     """
#     Return the messages about offer changes
#     """
#     # Look for changes in offers
#     offers_lost = set(offers_before.keys()).difference(
#         set(offers_after.keys()))
#     offers_gained = set(offers_after.keys()).difference(
#         set(offers_before.keys()))
#
#     # Build a list of (level, msg) tuples
#     offer_messages = []
#     for offer_id in offers_lost:
#         offer = offers_before[offer_id]
#         msg = render_to_string(
#             'basket/messages/offer_lost.html',
#             {'offer': offer})
#         offer_messages.append((
#             messages.WARNING, msg))
#     for offer_id in offers_gained:
#         offer = offers_after[offer_id]
#         msg = render_to_string(
#             'basket/messages/offer_gained.html',
#             {'offer': offer})
#         offer_messages.append((
#             messages.SUCCESS, msg))
#
#     # We use the 'include_buttons' parameter to determine whether to show the
#     # 'Checkout now' buttons.  We don't want to show these on the basket page.
#     msg = render_to_string(
#         'basket/messages/new_total.html',
#         {'basket': basket,
#          'include_buttons': False})#change for include_buttoms
#     offer_messages.append((
#         messages.INFO, msg))
#
#     return offer_messages



class BasketAddView(CoreBasketAddView):#FormView):
    """
    Handles the add-to-basket submissions, which are triggered from various
    parts of the site. The add-to-basket form is loaded into templates using
    a templatetag from module basket_tags.py.
    """
    # form_class = AddToBasketForm
    # product_model = get_model('catalogue', 'product')
    # add_signal = signals.basket_addition
    # http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        print len(request.POST['labels[]'])
        self.product = shortcuts.get_object_or_404(
            self.product_model, pk=kwargs['pk'])
        return super(BasketAddView, self).post(request, *args, **kwargs)

    # def get_form_kwargs(self):
    #     kwargs = super(BasketAddView, self).get_form_kwargs()
    #     kwargs['basket'] = self.request.basket
    #     kwargs['product'] = self.product
    #     return kwargs

    # def form_invalid(self, form):
    #     msgs = []
    #     for error in form.errors.values():
    #         msgs.append(error.as_text())
    #     clean_msgs = [m.replace('* ', '') for m in msgs if m.startswith('* ')]
    #     messages.error(self.request, ",".join(clean_msgs))
    #
    #     return redirect_to_referrer(self.request, 'basket:summary')

    # def form_valid(self, form):
    #     offers_before = self.request.basket.applied_offers()
    #
    #     self.request.basket.add_product(
    #         form.product, form.cleaned_data['quantity'],
    #         form.cleaned_options())
    #     messages.success(self.request, self.get_success_message(form),
    #                      extra_tags='safe noicon')
    #
    #     # Check for additional offer messages
    #     apply_messages(self.request, offers_before)
    #     # Send signal for basket addition
    #     self.add_signal.send(
    #         sender=self, product=form.product, user=self.request.user,
    #         request=self.request)
    # #
    #     return super(BasketAddView, self).form_valid(form)

    # def get_success_message(self, form):
    #     return render_to_string(
    #         'basket/messages/addition.html',
    #         {'product': form.product,
    #          'quantity': form.cleaned_data['quantity']})

    def get_success_url(self):
        post_url = self.request.POST.get('next')
        #print 'en el get_success_url'
        #print post_url
        if post_url and is_safe_url(post_url, self.request.get_host()):
            #print 'en el if del get_success_url'
            return post_url
        url2 = reverse('checkout:index')
        #url = safe_referrer(self.request, 'basket:summary')
        #print 'urls: '
        #print url
        #print url2
        return url2

#@receiver(basket_addition)
#def add_label():

