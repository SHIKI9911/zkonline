"""zkonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls import url, include

import xadmin

from apps.users.views import LoginView, LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('login/forgetpwd/', TemplateView.as_view(template_name='forgetpwd.html'), name='forgetpwd'),
    # user
    path('user_center/', TemplateView.as_view(template_name='user_center.html'), name='user_center'),
    path('user_message/', TemplateView.as_view(template_name='user_message.html'), name='user_message'),
    # course
    path('course_list/', TemplateView.as_view(template_name='course_list.html'), name='course_list'),
    # teacher
    path('teacher_list/', TemplateView.as_view(template_name='teacher_list.html'), name='teacher_list'),
    url(r'^captcha/', include('captcha.urls')),

]
