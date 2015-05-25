from django import forms

from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm, Product
#from oscar.core.loading import get_class, get_model

#Product = get_model('catalogue', 'Product')

class ProductForm(CoreProductForm):
    class Meta:
        model = Product
        fields = ['title', 'categories', 'structure'] #is_discountable, description, ups
        widgets = {
            'structure': forms.HiddenInput()
        }