# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='tickets',
            field=models.ManyToManyField(to='issues.Ticket', blank=True),
            preserve_default=True,
        ),
    ]
