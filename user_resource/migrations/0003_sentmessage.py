# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-06 02:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ('user_resource', '0002_auto_20150926_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]