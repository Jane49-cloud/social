from django import forms

from .models import Restaurant


# class CreateForm(forms.form):
#     name = forms.CharField(max_length= 250)
#     location=forms.CharField(required = False)
#     category = forms.CharField(required = False)


class ModelForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'location',
            'category',
            'image'
        ]
