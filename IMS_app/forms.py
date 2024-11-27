from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django import forms 
from .models import UserData

class UserForm(UserCreationForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'name': 'name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobileNumber = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'mob_no'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'name': 'password1'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = UserData
        fields = ['name','email','mobileNumber','password1','password2']



class LoginAuthentication(AuthenticationForm):
    username=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control w-100'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control w-100 py-1'}))