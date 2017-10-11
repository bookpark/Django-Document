# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0012_auto_20171011_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='recommender',
        ),
        migrations.AddField(
            model_name='membership',
            name='recommenders',
            field=models.ManyToManyField(blank=True, related_name='recommend_membership_set', to='model.Idol'),
        ),
    ]
