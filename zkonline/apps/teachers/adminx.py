import xadmin

from apps.teachers.models import Teacher


class TeacherAdmin(object):
    list_display = ['name', 'desc', 'gender', 'mobile_number', 'email', 'c_time', 'detail']
    # 后台默认显示
    search_fields = ['name', 'mobile_number', 'email']
    # 搜索
    list_filter = ['gender', 'c_time']
    # 过滤器
    list_editable = ['name', 'desc', 'gender', 'mobile_number', 'email', 'course_nums', 'detail']
    # 设置可编辑字段


xadmin.site.register(Teacher, TeacherAdmin)
