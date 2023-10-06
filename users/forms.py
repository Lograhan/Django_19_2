from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.core.exceptions import ValidationError

from catalog.forms import StyleFormMixin
from users.models import User
from users.utils import verify_mail


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'u_image', 'country')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password'].widget = forms.HiddenInput()


class MyAuthenticationForm(StyleFormMixin, AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if self.request.user.is_authenticated and not self.request.user.email_verify:
            verify_mail(self.request, self.user_cache)
            raise ValidationError(
                'Ваша почта не подтверждена. Проверьте email для завершения регистрации',
                code="invalid_login", )

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


