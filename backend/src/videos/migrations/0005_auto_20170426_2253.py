# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image_path',
            field=models.CharField(blank=True, default='https://angulardjango.s3-us-west-2.amazonaws.com/static/ang/assets/images/nature/4.jpg', max_length=120, null=True),
        ),
    ]