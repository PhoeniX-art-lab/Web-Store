from django import forms
from store.forms import PlaceholderForm

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class CartOrderForm(PlaceholderForm):
    city_choice = [('Brest', 'Brest'),
                   ('Vitebsk', 'Vitebsk'),
                   ('Gomel', 'Gomel'),
                   ('Grodno', 'Grodno'),
                   ('Mogilev', 'Mogilev'),
                   ('Minsk', 'Minsk'),
                   ('Minsk Region', 'Minsk Region')]
    name = forms.CharField(max_length=20, help_text="Your name")
    phone = forms.CharField(help_text="Your phone")
    city = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select-form'}), choices=city_choice)
    detail_address = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}),
                                     max_length=100, help_text="Enter street, house number, apartment")
