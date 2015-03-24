# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0010_auto_20150324_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addlabel',
            name='ticketstatus_ptr',
        ),
        migrations.DeleteModel(
            name='Addlabel',
        ),
    ]
