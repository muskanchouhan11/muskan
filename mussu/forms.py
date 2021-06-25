from django import forms
from home.models import Hrproject

class studentforms(forms.ModelForm):
    class Meta():
        model=Hrproject
        fields="__all__"

class profile(forms.ModelForm):
    class Meta():
        model=Hrproject
        fields=['fullname','img']

