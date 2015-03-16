# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('label_name', models.CharField(max_length=20, verbose_name='標籤名稱')),
                ('color', models.CharField(max_length=6, verbose_name='顏色')),
            ],
            options={
                'verbose_name': '標籤(Label)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('ticket_title', models.CharField(max_length=60, verbose_name='案件主題')),
                ('status', models.BooleanField(default=False, verbose_name='結案')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
            ],
            options={
                'verbose_name': '案件(Ticket)',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='label',
            name='tickets',
            field=models.ManyToManyField(to='issues.Ticket'),
            preserve_default=True,
        ),
    ]
