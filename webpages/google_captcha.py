from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
