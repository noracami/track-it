# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0013_auto_20150324_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('user', models.CharField(max_length=30, verbose_name='姓名')),
                ('content', models.CharField(blank=True, max_length=140, verbose_name='留言內容')),
                ('time', models.DateTimeField(verbose_name='建立時間', auto_now_add=True)),
                ('ticket', models.ForeignKey(to='issues.Ticket', related_name='commentofguest')),
            ],
            options={
                'verbose_name': '訪客留言(Comment)',
            },
            bases=(models.Model,),
        ),
    ]
