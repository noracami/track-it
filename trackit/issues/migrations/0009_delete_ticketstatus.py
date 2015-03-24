# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_delete_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicketStatus',
        ),
    ]
