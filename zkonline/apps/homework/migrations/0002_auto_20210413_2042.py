# Generated by Django 2.2 on 2021-04-13 20:42

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='m_time',
        ),
        migrations.RemoveField(
            model_name='homeworktask',
            name='m_time',
        ),
        migrations.AlterField(
            model_name='homework',
            name='comment',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='教师评语'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='homeworktask',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='正文'),
        ),
    ]
