# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20150318_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo_path',
            field=models.URLField(default='/static/img/user/supportmale-128.png', verbose_name='大頭照'),
            preserve_default=True,
        ),
    ]
