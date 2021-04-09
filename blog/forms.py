from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"}),
                "first_name": forms.TextInput(attrs={"class": "form-control"}),
                "last_name": forms.TextInput(attrs={"class": "form-control"}),
                "email": forms.EmailInput(attrs={"class": "form-control"})
                }
        labels = {"email" : "Email"}

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control", "autofocus": True, "autocomplete": "off"}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={"class": "form-control", "autofocus": True, "autocomplete": "off"}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["uname", "title", "descpt"]
        labels = {"descpt": "Description"}
        widgets = {"uname":forms.HiddenInput(attrs={"required": False}),
                "title":forms.TextInput(attrs={"class":"form-control"}),
                "descpt":forms.Textarea(attrs={"class":"form-control"}),
                }

class UserProfileForm(UserChangeForm):
    password = forms.CharField(strip=False, widget=forms.HiddenInput(attrs={"autofocus": True}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"}),
                "first_name": forms.TextInput(attrs={"class": "form-control"}),
                "last_name": forms.TextInput(attrs={"class": "form-control"}),
                "email": forms.EmailInput(attrs={"class": "form-control"})
                }

class AdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"