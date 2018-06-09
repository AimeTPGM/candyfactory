from django import forms
from .models import Candy

class CandyForm(forms.ModelForm):
    class Meta:
        model = Candy
        fields = ('flavor', 'description',)