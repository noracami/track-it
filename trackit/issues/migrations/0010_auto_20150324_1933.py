# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0009_delete_ticketstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category', models.CharField(verbose_name='類別', max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
            ],
            options={
                'verbose_name': '狀態(TicketStatus)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Addlabel',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='issues.TicketStatus', auto_created=True)),
                ('labels', models.CharField(verbose_name='標籤', max_length=30)),
            ],
            options={
                'verbose_name': '添加標籤(Addlabel)',
            },
            bases=('issues.ticketstatus',),
        ),
        migrations.AddField(
            model_name='ticketstatus',
            name='ticket',
            field=models.ForeignKey(related_name='ticketofstatus', to='issues.Ticket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticketstatus',
            name='user',
            field=models.ForeignKey(related_name='userchangestatus', to='issues.User'),
            preserve_default=True,
        ),
    ]
