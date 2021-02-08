import xadmin

from apps.users.models import UserProfile


class UserProfileAdmin(object):
    list_display = ['id', 'real_name', 'mobile_number', 'gender', 'email', 'is_superuser']
    # 后台默认显示
    search_fields = ['real_name', 'mobile_number', 'email']
    # 搜索
    list_filter = ['gender', 'date_joined']
    # 过滤器
    list_editable = ['real_name', 'mobile_number', 'gender', 'email']
    # 设置可编辑字段


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
