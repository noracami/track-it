# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20150316_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', models.CharField(verbose_name='留言內容', max_length=140, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
            ],
            options={
                'verbose_name': '留言(Comment)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('category', models.CharField(verbose_name='類別', max_length=30)),
                ('user', models.CharField(verbose_name='使用者', max_length=30)),
                ('labels', models.CharField(verbose_name='標籤', max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
            ],
            options={
                'verbose_name': '狀態(TicketStatus)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('account', models.CharField(unique=True, verbose_name='登入帳號', max_length=30)),
                ('name', models.CharField(verbose_name='姓名', max_length=10)),
                ('nickname', models.CharField(verbose_name='暱稱', max_length=40, blank=True)),
                ('member', models.CharField(verbose_name='身分', default='User', max_length=20)),
            ],
            options={
                'verbose_name': '使用者(User)',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='issues.User', related_name='Users'),
            preserve_default=True,
        ),
    ]
