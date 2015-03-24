# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0012_auto_20150324_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=30, verbose_name='類別')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
            ],
            options={
                'verbose_name': '狀態(TicketStatus)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RemoveLabel',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='issues.TicketStatus', serialize=False)),
                ('labels', models.ForeignKey(related_name='removefromticket', to='issues.Label')),
            ],
            options={
                'verbose_name': '取消標籤(RemoveLabel)',
            },
            bases=('issues.ticketstatus',),
        ),
        migrations.CreateModel(
            name='AddLabel',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='issues.TicketStatus', serialize=False)),
                ('labels', models.ForeignKey(related_name='addtoticket', to='issues.Label')),
            ],
            options={
                'verbose_name': '添加標籤(AddLabel)',
            },
            bases=('issues.ticketstatus',),
        ),
        migrations.CreateModel(
            name='UserAssign',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='issues.TicketStatus', serialize=False)),
                ('user', models.ForeignKey(related_name='userassigned', to='issues.User')),
            ],
            options={
                'verbose_name': '人員指派(UserAssign)',
            },
            bases=('issues.ticketstatus',),
        ),
        migrations.CreateModel(
            name='UserUnassign',
            fields=[
                ('ticketstatus_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='issues.TicketStatus', serialize=False)),
                ('user', models.ForeignKey(related_name='userunassigned', to='issues.User')),
            ],
            options={
                'verbose_name': '取消人員指派(UserUnassign)',
            },
            bases=('issues.ticketstatus',),
        ),
        migrations.AddField(
            model_name='ticketstatus',
            name='maker',
            field=models.ForeignKey(related_name='userchangestatus', to='issues.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticketstatus',
            name='ticket',
            field=models.ForeignKey(related_name='ticketofstatus', to='issues.Ticket'),
            preserve_default=True,
        ),
    ]
