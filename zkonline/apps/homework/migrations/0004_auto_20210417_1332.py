# Generated by Django 2.2 on 2021-04-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_auto_20210413_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworktask',
            name='homework_num',
            field=models.IntegerField(default=0, verbose_name='提交人数'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='score',
            field=models.IntegerField(default=-1, verbose_name='得分'),
        ),
    ]
