from django import forms
from captcha.fields import CaptchaField
class Loginform(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码不正确'})

class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码不正确'})

class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)