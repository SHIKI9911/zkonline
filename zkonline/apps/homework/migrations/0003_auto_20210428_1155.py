# Generated by Django 2.2 on 2021-04-28 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20210418_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='提交者'),
        ),
    ]