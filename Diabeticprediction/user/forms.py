from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    Captcha = ReCaptchaField( label='Captcha')
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    Captcha = ReCaptchaField( label='Captcha*')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']




class CustomPasswordChangeForm(PasswordChangeForm):
    # Add custom styles, placeholders, or validation if needed
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter old password'}),
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
        help_text='Your password must contain at least 8 characters.'
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']

