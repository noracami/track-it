# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_comment_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='opened_user',
            field=models.ForeignKey(related_name='OpenedUser', default=1, to='issues.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=56, verbose_name='密碼', default='71454996db126e238e278a202a7dbc49dda187ec4f8c9dfc95584900'),
            preserve_default=True,
        ),
    ]
