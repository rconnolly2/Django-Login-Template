from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.login_web, name="login"),
    path("registrar/", views.registrar, name="registrar"),
    # Endpoints de django
    path("change-password/", auth_views.PasswordChangeView.as_view()),
    # Endpoints de OTP
    path('accounts/login/', LoginView.as_view(authentication_form=OTPAuthenticationForm)),
    path('verify-otp/', views.otp_login_view, name='verify_otp'),
]