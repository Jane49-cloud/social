from django import forms
from .models import Item
from Restaurants.models import Restaurant


class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields =[         
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]
        
        #passing user to the form
    def __init__(self, user=None, *args, **kwargs): 
        # print(kwargs.pop('user'))
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user)  #gives restaurant added by the customer only
        
     