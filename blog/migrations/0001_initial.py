# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('test', models.CharField(max_length=20)),
            ],
        ),
    ]
