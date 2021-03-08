from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

'''1、实体间的关系：一对多，多对多。
课程-评论：一个课程可以有多个评论
收藏-课程：一个收藏对应多个课程
我的课程-课程：每个用户可以学习多个课程
通知：每个用户可以接收多个通知

2、实体的具体字段
3、每个字段的类型，是否必填（默认为必填）'''

UserProfile = get_user_model()

# class Banner(BaseModel):
#     title = models.CharField(max_length=100, verbose_name="标题")
#     image = models.ImageField(upload_to="banner/%Y/%m", max_length=200, verbose_name="轮播图")
#     url = models.URLField(max_length=200, verbose_name="访问地址")
#     index = models.IntegerField(default=0, verbose_name="顺序")
#
#     class Meta:
#         verbose_name = "轮播图"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.title

class CourseComment(BaseModel):  # 课程评论
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    content = models.CharField(max_length=500, verbose_name='评论内容')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = '课程评论'

    def __str__(self):
        return self.content


class UserFavorite(BaseModel):  # 用户收藏
    fav_id = models.IntegerField(verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '教师'),), default=1, verbose_name='收藏类型')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = '用户收藏'


class UserMessage(BaseModel):  # 通知
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    content = models.CharField(max_length=500, verbose_name='通知内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')

    class Meta:
        verbose_name = '通知'
        verbose_name_plural = '通知'

    def __str__(self):
        return self.content


class UserCourses(BaseModel):  # 用户学习的课程
    is_finished = models.BooleanField(default=False, verbose_name='是否完成')
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '我的课程'
        verbose_name_plural = '我的课程'
