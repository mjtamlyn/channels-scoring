# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number_of_rounds', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoundScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.PositiveIntegerField()),
                ('score', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0, editable=False)),
                ('position', models.PositiveIntegerField(default=0, editable=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.Player')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='roundscore',
            unique_together=set([('score', 'round_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('game', 'player')]),
        ),
    ]
