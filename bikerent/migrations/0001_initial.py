# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeDetail',
            fields=[
                ('bike_id', models.AutoField(serialize=False, primary_key=True)),
                ('vehicle_number', models.CharField(unique=True, max_length=20)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('year_of_reg', models.IntegerField(max_length=4)),
                ('passing', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
                ('daily_rate', models.IntegerField(max_length=10)),
                ('isactive', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
