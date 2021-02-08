import xadmin

from apps.operations.models import CourseComment, UserFavorite, UserMessage, UserCourses


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'content']
    # 后台默认显示
    search_fields = ['user', 'course']
    # 搜索
    list_filter = ['user', 'course']
    # 过滤器
    list_editable = ['user', 'course', 'content']
    # 设置可编辑字段


class UserFavoriteAdmin(object):
    list_display = ['fav_id', 'fav_type']
    # 后台默认显示
    search_fields = ['fav_id', 'fav_type']
    # 搜索
    list_filter = ['fav_id', 'fav_type']
    # 过滤器
    list_editable = ['fav_id', 'fav_type']
    # 设置可编辑字段


class UserMessageAdmin(object):
    list_display = ['user', 'content', 'has_read']
    # 后台默认显示
    search_fields = ['user', 'content']
    # 搜索
    list_filter = ['user', 'content', 'has_read']
    # 过滤器
    list_editable = ['user', 'content', 'has_read']
    # 设置可编辑字段


class UserCoursesAdmin(object):
    list_display = ['is_finished', 'user', 'course']
    # 后台默认显示
    search_fields = ['user', 'course']
    # 搜索
    list_filter = ['is_finished', 'user', 'course']
    # 过滤器
    list_editable = ['is_finished', 'user', 'course']
    # 设置可编辑字段


xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourses, UserCoursesAdmin)
