# Generated by Django 2.2 on 2021-04-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_expcomment_userexp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='url',
        ),
    ]