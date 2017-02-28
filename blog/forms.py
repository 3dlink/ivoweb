from django import forms

class FormBusqueda(forms.Form):
   consulta = forms.CharField(max_length = 50)