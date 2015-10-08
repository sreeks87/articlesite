# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postarticle',
            name='opt_img',
            field=models.ImageField(null=True, upload_to='image', blank=True),
        ),
    ]
