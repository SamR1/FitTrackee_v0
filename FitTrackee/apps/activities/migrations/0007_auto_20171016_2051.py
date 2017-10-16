# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 18:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0006_auto_20171010_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comments',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='likes',
            field=models.ManyToManyField(related_name='activity_users_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_users_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]