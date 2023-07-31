from django import forms

from core.models import Mobile, Brand


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['model_name', 'color', 'country', 'price', 'size', 'is_available']

    def __init__(self, *args, **kwargs):
        super(MobileForm, self).__init__(*args, **kwargs)
        self.fields['brand_name'] = forms.CharField()
        self.fields['brand_country'] = forms.CharField()

    def save(self, commit=True):
        super(MobileForm, self).save(commit=False)
        brand_name = self.cleaned_data.pop('brand_name')
        brand_country = self.cleaned_data.pop('brand_country')

        brand, created = Brand.objects.get_or_create(name=brand_name, nationality=brand_country)
        self.cleaned_data['brand'] = brand
        m = Mobile.objects.create(**self.cleaned_data)
        return m


