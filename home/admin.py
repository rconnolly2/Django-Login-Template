from django.contrib import admin
from .models import Post
from django_otp.admin import OTPAdminSite
# Register your models here.
admin.site.register(Post)
# --- 2FA ---
admin.site.__class__ = OTPAdminSite