import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'category', 'tag', 'detail', 'learn_times', 'click_nums', 'student_nums', 'notice', 'lesson_nums', 'course_img']
    # 后台默认显示
    search_fields = ['name', 'tag', 'category']
    # 搜索
    list_filter = ['tag', 'category']
    # 过滤器
    list_editable = ['name', 'notice', 'tag', 'detail', 'category', 'course_img']
    # 设置可编辑字段

    inlines = [LessonInline,CourseResourceInline]  #增加章节和课程资源, 添加课程的时候，可以直接添加章节和课程资源

class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_times' ]
    # 后台默认显示
    search_fields = ['course', 'name']
    # 搜索
    list_filter = ['course', 'name', 'learn_times']
    # 过滤器
    list_editable = ['course', 'name', 'learn_times']
    # 设置可编辑字段


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'learn_times', 'url']
    # 后台默认显示
    search_fields = ['lesson', 'name', 'learn_times']
    # 搜索
    list_filter = ['lesson', 'name', 'learn_times']
    # 过滤器
    list_editable = ['lesson', 'name', 'learn_times', 'url']
    # 设置可编辑字段


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file']
    # 后台默认显示
    search_fields = ['course', 'name']
    # 搜索
    list_filter = ['course', 'name']
    # 过滤器
    list_editable = ['course', 'name', 'file']
    # 设置可编辑字段


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

