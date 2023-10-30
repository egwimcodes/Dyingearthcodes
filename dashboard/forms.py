from django.contrib.auth.forms import UserCreationForm
from .models import User, Sensor, TodoApp
from django import forms
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    country = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'country']


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'country', 'city', 'zip_code', 'avatar']


class SensorListForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'location']


class UpdateTodoForm(ModelForm):
    class Meta:
        model = TodoApp
        fields = ['text', 'done', 'time']

























