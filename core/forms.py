from django import forms
from django.forms import fields
from .models import Arriendo

class ArriendoForm(forms.ModelForm):

    class Meta:
        model = Arriendo
        fields = '__all__'
