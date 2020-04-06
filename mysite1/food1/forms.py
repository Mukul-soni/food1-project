from django import forms
from .models import Itm
class ItmForm(forms.ModelForm):
    class Meta:
        model = Itm
        fields = ['Itm_name','Itm_dec','Itm_price','Itm_image']