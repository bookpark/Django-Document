# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0008_auto_20171010_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('friends', models.ManyToManyField(blank=True, null=True, related_name='_facebookuser_friends_+', to='model.FacebookUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='twitteruser',
            name='friends',
        ),
        migrations.DeleteModel(
            name='TwitterUser',
        ),
    ]