# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_user_photo_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], max_length=2, default='FR')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='label',
            name='fontcolor',
            field=models.CharField(choices=[('ffffff', '白'), ('000000', '黑')], verbose_name='字的顏色', max_length=6, default='ffffff'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(choices=[('MAIN', (('e11d21', '紅色'), ('eb6420', '橙色'), ('fbca04', '黃色'), ('009800', '綠色'), ('006b75', '暗綠色'), ('207de5', '藍色'), ('0052cc', '暗藍色'), ('5319e7', '紫色'))), ('LIGHT', (('f7c6c7', '紅色'), ('fad8c7', '橙色'), ('fef2c0', '黃色'), ('bfe5bf', '綠色'), ('bfdadc', '暗綠色'), ('c7edf8', '藍色'), ('bfd4f2', '暗藍色'), ('d4c5f9', '紫色')))], verbose_name='顏色', max_length=6, default='e11d21'),
            preserve_default=True,
        ),
    ]
