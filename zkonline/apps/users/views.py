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


def hash_code(s, salt='zkonline'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            login_form = Login_Form()
            return render(request, 'login.html', locals())

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


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        register_form = RegisterForm()
        # 如果已登录，则返回首页
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'register.html', {"register_form": register_form})

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        msg = "请检查填写的内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            mobile_number = register_form.cleaned_data['mobile_number']

            if password1 != password2:  # 判断两次密码是否相同
                msg = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = UserProfile.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    msg = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = UserProfile.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    msg = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())
                same_mobile_user = UserProfile.objects.filter(mobile_number=mobile_number)
                if same_mobile_user or len(mobile_number) != 11:
                    msg = "该手机号不正确或已注册"
                    return render(request, 'register.html', locals())

                # 将数据存入数据库
                new_user = UserProfile.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.gender = sex
                new_user.mobile_number = mobile_number
                new_user.save()
                # 登陆
                login(request, new_user)
                return render(request, 'index.html')  # 自动跳转到登录页面

        else:
            register_form = RegisterForm()
            return render(request, 'register.html', {
                "register_form": register_form,
            })

