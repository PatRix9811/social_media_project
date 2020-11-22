"""YooloFriends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import login_view, register_view, logout_view, user_home_view, user_messages_view, user_conversations_view
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('',login_view, name = 'login'),
    path('register', register_view, name = 'register'),
    path('logout', logout_view, name = 'logout'),
    path('profile', user_home_view, name = 'user_home'),
    path('conversations', user_conversations_view, name='conversations'),
    path('conversations/<conv>', user_messages_view, name = 'messages'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
