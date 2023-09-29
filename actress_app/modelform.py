from django import forms
from .models import *

class Emma_model_form(forms.ModelForm):
    class Meta:
        model = Emma
        fields = '__all__'

class Krish_model_form(forms.ModelForm):
    class Meta:
        model = Krish
        fields = '__all__'

class Aish_model_form(forms.ModelForm):
    class Meta:
        model = Aish
        fields = '__all__'

class Ananya_model_form(forms.ModelForm):
    class Meta:
        model = Ananya
        fields = '__all__'