# users.view
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
import hashlib
from apps.users.models import UserProfile

from apps.users.forms import Login_Form, RegisterForm


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


# def hash_code(s, salt='zkonline'):
#     h = hashlib.sha256()
#     s += salt
#     h.update(s.encode())  # update方法只接收bytes类型
#     return h.hexdigest()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # 表单验证
        login_form = Login_Form(request.POST)

        if login_form.is_valid():
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # 用户名密码的验证
            user = authenticate(username=user_name, password=password)
            if user is not None:
                # 查询到用户, 使用该方法可以不用管session等细节
                login(request, user)
                # 登陆成功之后如何返回页面
                # return render(request, 'index.html') # render的使用有细节不完善
                return HttpResponseRedirect(reverse("index"))
            else:
                # 未查询到用户, 保持在原来页面并做出提示
                return render(request, 'login.html', {"msg": "用户名或密码错误", "login_form": login_form})

        else:
            return render(request, "login.html",  {"msg": "用户名或密码错误", "login_form": login_form})


def register(request):
    pass