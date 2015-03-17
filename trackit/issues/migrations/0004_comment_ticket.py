# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_auto_20150317_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(to='issues.Ticket', default=1, related_name='Tickets'),
            preserve_default=False,
        ),
    ]
