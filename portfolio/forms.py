from django import forms
from .models import Orcamento

class OrcamentoForm(forms.ModelForm):
    
    class Meta:
        model = Orcamento
        fields = ['nome', 'email', 'telefone', 'mensagem']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
        
