from oscar.apps.promotions.views import HomeView as CoreHomeView


class HomeView(CoreHomeView):

    template_name = 'promotions/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        request.META["CSRF_COOKIE_USED"] = True
        return self.render_to_response(context)