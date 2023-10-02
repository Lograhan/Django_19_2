from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, VerifyEmailView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/', TemplateView.as_view(template_name='user/verification.html'),  name='verify'),
    path('verify_email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email')
]