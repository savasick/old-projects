from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import Account
#from captcha.fields import CaptchaField

class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({ 'id': 'username', 'class': 'form-control form-control-lg', 'autofocus': True })
        self.fields['email'].widget.attrs.update({ 'id': 'email', 'class': 'form-control form-control-lg' })
        self.fields['password1'].widget.attrs.update({ 'id': 'password', 'class': 'form-control form-control-lg' })
        #self.fields['captcha'].widget.attrs.update({ 'id': 'captcha', 'class': 'form-control form-control-lg' })
        del self.fields['password2']
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({ 'id': 'username', 'class': 'form-control form-control-lg', 'autofocus': True })
        self.fields['password'].widget.attrs.update({ 'id': 'password', 'class': 'form-control form-control-lg' })
        #self.fields['captcha'].widget.attrs.update({ 'id': 'captcha', 'class': 'form-control form-control-lg' })

class AccountUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(label=('Avatar'),required=False, widget=forms.FileInput)
    class Meta:
        model = Account
        fields = ['avatar', 'nickname', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'form-control', 'accept': ".jpg, .jpeg, .png", 'type': 'file'})
        self.fields['nickname'].widget.attrs.update({'class': 'form-control'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})

class PasswordForm(PasswordChangeForm):
    class Meta:
        model = Account
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({ 'class': 'form-control', 'autofocus': True })
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})