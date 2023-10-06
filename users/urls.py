from django.urls import path, include
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, VerifyEmailView, MyLoginView, UserForgotPasswordView, \
    UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/', TemplateView.as_view(template_name='users/verification.html'),  name='verify'),
    path('verify_email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('verification_failure/', TemplateView.as_view(template_name='users/verification_failure.html'),  name='verification_failure'),
    path('verification_success/', TemplateView.as_view(template_name='users/verification_success.html'),  name='verification_success'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/', TemplateView.as_view(template_name='users/password_confirm.html'),  name='password_confirm'),

]