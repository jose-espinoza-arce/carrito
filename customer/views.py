from django.conf import settings

from oscar.apps.customer.views import AccountAuthView as CoreAccountAuthView, ProfileDeleteView as CoreProfileDeleteView


class AccountAuthView(CoreAccountAuthView):
    """
    This is actually a slightly odd double form view that allows a customer to
    either login or register.
    + succes register redirect url
    """

    def get_registration_success_url(self, form):
        redirect_url = form.cleaned_data['redirect_url']
        if redirect_url:
            return redirect_url
        return settings.LOGIN_REDIRECT_URL

class ProfileDeleteView(CoreProfileDeleteView):
    page_title = _('Eliminar Peril')