# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 5, 21, 11, 969179, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
