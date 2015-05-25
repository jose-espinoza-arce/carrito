from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as CoreProductCreateUpdateView


class ProductCreateUpdateView(CoreProductCreateUpdateView):
    pass
    #def dispatch(self, request, *args, **kwargs):
    #    print request
    #    resp = super(CoreProductCreateUpdateView, super(ProductCreateUpdateView, self)).dispatch(
    #        request, *args, **kwargs)
    #    #print resp
    #    return self.check_objects_or_redirect() or resp