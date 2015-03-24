# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_auto_20150324_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketstatus',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='ticketstatus',
            name='user',
        ),
        migrations.DeleteModel(
            name='TicketStatus',
        ),
        migrations.AddField(
            model_name='ticket',
            name='assignee',
            field=models.ManyToManyField(to='issues.User', blank=True),
            preserve_default=True,
        ),
    ]
