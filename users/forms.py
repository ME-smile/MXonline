from django import forms
from captcha.fields import CaptchaField
class Loginform(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField()