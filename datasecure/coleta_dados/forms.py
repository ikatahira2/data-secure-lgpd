from django import forms
from .models import DadosUsuario

class DadosUsuarioForm(forms.ModelForm):
    class Meta:
        model = DadosUsuario
        fields = ['nome', 'email', 'telefone', 'consentimento']
