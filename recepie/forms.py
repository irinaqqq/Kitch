from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from recepie.models import UserExtended

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    first_name = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    last_name = forms.CharField(max_length=60, required= False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Почта')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Потдверждение пароля')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password')

class UserExtendedCreationForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ('profile_image',)

    def save(self, user):
        user.userextended.profile_image = self.cleaned_data['profile_image']
        user.userextended.save() 

class UserExtendedUpdateForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ('profile_image',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class UserChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )

    new_password1 = forms.CharField(
        label=("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    new_password2 = forms.CharField(
        label=("Confirm password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('old_password', 'new_password2', 'new_password2')

    def is_valid(self):
        if self.data['new_password1'] != self.data['new_password2']:
            return False
        
        old_pass = self.data['old_password'] 
        if not self.user.check_password(old_pass):
            return False

        return super(UserChangePasswordForm, self).is_valid()

    def save(self):
        if self.is_valid():
            self.user.set_password(self.cleaned_data['new_password1'])
            self.user.save()
            return self.user