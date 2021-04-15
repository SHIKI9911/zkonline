from apps.users.models import UserProfile
from django.contrib.auth import get_user_model
import xadmin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
                                       AdminPasswordChangeForm, PasswordChangeForm)
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *


# # 获取全局user模型
# User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ("username", 'real_name', 'mobile_number', 'gender', 'email',)
        field_classes = {"username": UsernameField, }


class UserProfileAdmin(object):
    list_display = ['id','username', 'real_name', 'mobile_number', 'gender', 'email', 'is_superuser']
    # 后台默认显示
    search_fields = ['real_name', 'mobile_number', 'email']
    # 搜索
    list_filter = ['gender', 'date_joined']
    # 过滤器
    list_editable = ['real_name', 'mobile_number', 'gender', 'email']
    # 设置可编辑字段

    # 配置表单
    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = MyUserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserProfileAdmin, self).get_model_form(**kwargs)


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
