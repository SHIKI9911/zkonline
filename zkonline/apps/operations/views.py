from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.http import JsonResponse

from apps.operations.models import UserCourses, CourseComment
from apps.courses.models import Course


class AddCommentsView(View):
    '''用户评论'''
    def post(self, request):
        # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
        if not request.user.is_authenticated:
            return JsonResponse({
                "status": "fail",
                "msg": "用户未登录"
            })

        course_id = int(request.POST.get("course"))
        content = request.POST.get("content")

        if course_id > 0 and content:
            course= Course.objects.get(id = course_id )

            comment = CourseComment()
            comment.user = request.user
            comment.content = content
            comment.course = course
            comment.save()

            return JsonResponse({
                "status": "success",
            })

        else:
            return JsonResponse({
                "status": "fail",
                "msg": "评论失败"
            })


