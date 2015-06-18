from oscar.apps.basket.views import BasketAddView as CoreBasketAddView, apply_messages

from django.core.urlresolvers import reverse

from django import shortcuts

from django.utils.http import is_safe_url

from django.dispatch.dispatcher import receiver
from oscar.apps.basket.signals import basket_addition

from oscar.core.utils import safe_referrer

from django.contrib import messages
#from django.shortcuts import redirect
from django.template.loader import render_to_string

from dashboard.cmproducts.models import Tag





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
        print 'my.basket.views.BasketAddView.post'
        print request.POST.getlist('labels[]')
        self.product = shortcuts.get_object_or_404(
            self.product_model, pk=kwargs['pk'])
        return super(BasketAddView, self).post(request, *args, **kwargs)

    def form_valid(self, form):

        offers_before = self.request.basket.applied_offers()

        self.request.basket.add_product(
            form.product, form.cleaned_data['quantity'],
            form.cleaned_options())

        messages.success(self.request, self.get_success_message(form),
                         extra_tags='safe noicon')

        # Check for additional offer messages
        apply_messages(self.request, offers_before)

        # Send signal for basket addition
        self.add_signal.send(
            sender=self, product=form.product, user=self.request.user,
            request=self.request)

        print 'my.basket.views.BasketAddView.form_valid'
        print dir(self.request.basket)
        print self.request.basket.all_lines()
        print super(BasketAddView, self)

        lines = self.request.basket.all_lines()

        assert len(lines) == 1, "Hay mas de dos tipos de productos en la canasta"
        try:
            line = lines[-1]
        except:
            line = lines[0]
        labels = self.request.POST.getlist('labels[]')

        assert len(labels) > 0, 'No hay etiquetas personalizadas'

        for label_id in labels:
            label = Tag.objects.get(pk=label_id)
            label.line = line
            label.save()
            print label


        return super(CoreBasketAddView, self).form_valid(form)



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

