from django import forms

from .models import *

class ConsorcioForm(forms.ModelForm):
    class Meta:
        model = Consorcio
        fields = '__all__'

class AdministradoraForm(forms.ModelForm):
    class Meta:
        model = Administradora
        fields = '__all__'

class RegraComissionamentoForm(forms.ModelForm):
    class Meta:
        model = RegraComissionamento
        fields = '__all__'

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = '__all__'

class FinanciamentoForm(forms.ModelForm):
    class Meta:
        model = Financiamento
        fields = '__all__'

class HomeEquityForm(forms.ModelForm):
    class Meta:
        model = HomeEquity
        fields = '__all__'