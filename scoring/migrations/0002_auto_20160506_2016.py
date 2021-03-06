# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundscore',
            name='value',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roundscore',
            name='score',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.Score'),
        ),
        migrations.AlterField(
            model_name='score',
            name='position',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
    ]
