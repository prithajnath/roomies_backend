# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-12 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomies', '0004_usermatches'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'', verbose_name='defaultpic.png')),
            ],
        ),
    ]
