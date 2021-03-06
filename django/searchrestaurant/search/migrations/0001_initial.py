# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_location', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('restaurant_type', models.CharField(default='pizza', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('address', models.CharField(max_length=500)),
                ('checkins', models.IntegerField()),
                ('photo_url', models.CharField(max_length=800)),
                ('venue_id', models.CharField(max_length=500)),
                ('phone_number', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('r_type', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('-checkins',),
            },
        ),
        migrations.AddField(
            model_name='location',
            name='restaurant',
            field=models.ManyToManyField(to='search.Restaurant'),
        ),
    ]
