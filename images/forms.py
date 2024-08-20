from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extentions = ['jpg', 'jpeg', 'png']
        extention = url.rsplit('.', 1)[1].lower()
        if extention not in valid_extentions:
            raise forms.ValidationError('The given URL does not match valid image extentions.')

        return url        