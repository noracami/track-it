# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0014_guestcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloseIssue',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, parent_link=True, to='issues.TicketStatus')),
            ],
            options={
                'verbose_name': '結束案件',
            },
            bases=('issues.ticketstatus',),
        ),
        migrations.CreateModel(
            name='ReopenIssue',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, parent_link=True, to='issues.TicketStatus')),
            ],
            options={
                'verbose_name': '重啟案件',
            },
            bases=('issues.ticketstatus',),
        ),
    ]
