from django import forms

class FormularioLogin(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    tlf = forms.IntegerField(max_value=999999999)
    contraseña = forms.CharField(max_length=200)