from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.models import BaseModel


class Teacher(BaseModel):
    gender_choices = (('male', '男'),
                      ('female', '女'))

    name = models.CharField(max_length=20, verbose_name='教师名称', null=False)
    desc = models.TextField(verbose_name='教师简介')
    profile = models.ImageField(upload_to='profile_img/teacher/%Y/%m', verbose_name='头像', max_length=100,
                                default='/profile_img/teacher/default_profile.png')
    gender = models.CharField(verbose_name='性别', choices=gender_choices, max_length=6)
    mobile_number = models.CharField(max_length=11, null=False, unique=True, verbose_name='手机号码')
    email = models.EmailField(verbose_name='邮箱', unique=True)
    course_nums = models.IntegerField(default=0, verbose_name='课程数')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'

    def __str__(self):
        return self.name
