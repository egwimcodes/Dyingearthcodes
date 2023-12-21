from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, Sensor, TodoApp
from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .countries import COUNTRY_CHOICES



class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'name':'username'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'name':'first name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'name':'last name'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'name':'email'}))
    zip_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip code', 'name':'zip code'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'name':'password1'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password','name':'password2'}))
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Country','name':'country'}))
    receive_marketing_mails = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'name':'receive_marketing_mails'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'zip_code', 'password1', 'password2', 'country', 'receive_marketing_mails']
    def clean(self):
        cleaned_data = super().clean()
        
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        zip_code = cleaned_data.get('zip_code')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        country = cleaned_data.get('country')
        receive_marketing_mails = cleaned_data.get('receive_marketing_mails')

        if username and not username.isalnum():
            self.add_error('username', 'Username must contain only letters and numbers.')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use.')
        if country and not country.isalnum():
            self.add_error('country', 'Country must contain only letters')
            
        return cleaned_data


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        # Remove the help text from the fields
        for field_name in self.fields:
            self.fields[field_name].help_text = None


class DeleteAccountForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'name':'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Comfirm Password', 'name':'password'}))
    
    
    class Meta:
        model = get_user_model()
        fields = []
        
        
    def __init__(self, request, *args, **kwargs):
        super(DeleteAccountForm, self).__init__(*args, **kwargs)
        self.request = request
        
    def clean(self):
        cleaned_data = super().clean()
        email = self.changed_data.get('email')  
        password = self.cleaned_data.get('password')
        
        if not request.user.email == email:
            self.add_error('email', 'Email is Invalid')
        if not request.user.password == password:
            self.add_error('password', 'Password is incorrect')
        
        return cleaned_data
        
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'readonly': 'readonly'}), required=False)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name', 'readonly': 'readonly' }), required=False)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name', 'readonly': 'readonly' }), required=False)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'readonly': 'readonly' }), required=False)
    phone  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'phone', 'readonly': 'readonly' }), required=False)
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'address', 'readonly': 'readonly' }), required=False)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Country','readonly': 'readonly', 'name':'country'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'city', 'readonly': 'readonly' }), required=False)
    zip_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'zip_code', 'readonly': 'readonly' }), required=False)
    avatar = forms.FileField(max_length=100, widget=forms.FileInput(attrs={'class': 'form-control', 'name': 'avatar', 'readonly': 'readonly' }), required=False)
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'country', 'city', 'zip_code', 'avatar']


class RegisterSensorForm(forms.Form):
    new_sensor_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'new_sensor_name', 'required':'required'}))
    sensor_location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'sensor_location', 'required':'required'}))
    sensor_qr = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mt-3 mx-auto', 'name': 'sensor_code','style':'font-size: 20px', 'id': '1','required':'required', "placeholder": "DE - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX - XXXXX"}))
    
    class Meta:
        fields = ['new_sensor_name', 'sensor_location', 'sensor_qr']


class SensorListForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'location']


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['text', 'done', 'time']

























