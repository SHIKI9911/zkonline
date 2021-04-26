# Generated by Django 2.2 on 2021-04-17 17:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiments', '0002_auto_20210417_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.Experiment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户实验关联',
                'verbose_name_plural': '用户实验关联',
            },
        ),
        migrations.CreateModel(
            name='ExpComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('content', models.CharField(max_length=500, verbose_name='评论内容')),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.Experiment', verbose_name='实验')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '实验评论',
                'verbose_name_plural': '实验评论',
            },
        ),
    ]