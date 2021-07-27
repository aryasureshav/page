from django import forms
from . models import Register
class SignupForm(forms.ModelForm):
	Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
	ConfirmPassword=forms.CharField(max_length=8,widget=forms.PasswordInput)
	class Meta():
		model=Register
		fields='__all__'

class LoginForm(forms.ModelForm):
	Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
	class Meta():
		model=Register
		fields=('Email','Password')

class UpdateForm(forms.ModelForm):

	class Meta():
		model=Register
		fields=('Name','Age','Email','Photo')

class ChangePasswordForm(forms.Form):
	OldPassword=forms.CharField(max_length=8,widget=forms.PasswordInput)
	NewPassword=forms.CharField(max_length=8,widget=forms.PasswordInput)
	ConfirmPassword=forms.CharField(max_length=8,widget=forms.PasswordInput)
