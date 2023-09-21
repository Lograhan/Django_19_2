from django import forms

from catalog.models import Product, Version

ban = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_name', 'p_description', 'p_image', 'p_category', 'p_price')

    def clean_p_name(self):
        cleaned_data = self.cleaned_data['p_name']

        for name in ban:
            if name in cleaned_data:
                raise forms.ValidationError('Недопустимое слово')

        return cleaned_data

    def clean_p_description(self):
        cleaned_data = self.cleaned_data['p_description']

        for desc in ban:
            if desc in cleaned_data:
                raise forms.ValidationError('Недопустимое слово')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

