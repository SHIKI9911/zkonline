from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger

from apps.courses.models import Course, Lesson, Video, CourseResource



class CourseListView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_courses = Course.objects.order_by("-c_time")
        courses_nums = Course.objects.all().count()

        # 对课程机构数据进行分页
        # 如果没有页面，则显示一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 每页显示的记录条数
        p = Paginator(all_courses, per_page=5, request=request)
        courses = p.page(page)

        return render(request, "course_list.html", {
            "all_courses": courses,
            "courses_nums": courses_nums,
        })




