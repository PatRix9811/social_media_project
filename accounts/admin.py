from django.contrib import admin
from .models import Profile

class AdminProfile(admin.ModelAdmin):
	fields  = ['user', 'image','conversations', 'messages',]


admin.site.register(Profile, AdminProfile)