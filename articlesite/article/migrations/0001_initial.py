# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('body_txt', models.TextField()),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
                ('article_cat', models.CharField(max_length=50)),
                ('hero_img', models.ImageField(upload_to='image')),
                ('opt_img', models.ImageField(upload_to='image')),
            ],
        ),
    ]
