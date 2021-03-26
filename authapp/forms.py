from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser
from django.contrib.auth.models import User


class AuthUserLoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")


class AuthUserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("username", "password")

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user