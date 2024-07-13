from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=20, required=True, label="Marca") # campo requerido
    modelo = forms.CharField(max_length=20, required=True, label="Modelo") # campo requerido
    matricula = forms.CharField(max_length=20, required=True, label="Matricula") # campo requerido 

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, label="Nombre") # campo requerido
    apellido = forms.CharField(max_length=60, required=True, label="Apellido") # campo requerido
    email = forms.EmailField(required=True) # campo requerido
    direccion = forms.CharField(max_length=100, required=True, label="Dirección") # campo requerido

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, label="Nombre") # campo requerido
    apellido = forms.CharField(max_length=60, required=True, label="Apellido") # campo requerido
    email = forms.EmailField(required=True) # campo requerido

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, label="Nombre") # campo requerido
    apellido = forms.CharField(max_length=60, required=True, label="Apellido") # campo requerido
    documento = forms.CharField(max_length=20, required=True, label="Documento") # campo requerido

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=16, required=True, label="Contraseña", widget=forms.PasswordInput, ) 
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput, max_length=16, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditoForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True, label="Nombre") 
    last_name = forms.CharField(label="Apellido", max_length=560, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
