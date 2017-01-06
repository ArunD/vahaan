# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bikerent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_superuser', models.IntegerField(default=0)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('date_joined', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BikeAvailability',
            fields=[
                ('bike_type_id', models.IntegerField(serialize=False, primary_key=True)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('avail_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'bike_availability',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BikeType',
            fields=[
                ('bike_type_id', models.IntegerField(serialize=False, primary_key=True)),
                ('vehicle_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bike_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DummyTbl',
            fields=[
                ('dummy_data', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'dummy_tbl',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('transaction_id', models.IntegerField(serialize=False, primary_key=True)),
                ('bike_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'transaction_detail',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisitCount',
            fields=[
                ('count_id', models.IntegerField(serialize=False, primary_key=True)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'visit_count',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('snippet', models.CharField(max_length=150, blank=True)),
                ('body', models.TextField(max_length=10000, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(blank=True)),
                ('remind', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BikeDetail',
        ),
        migrations.CreateModel(
            name='BikeDetail',
            fields=[
                ('bike_id', models.IntegerField(serialize=False, primary_key=True)),
                ('bike_type_id', models.IntegerField()),
                ('vehicle_number', models.CharField(unique=True, max_length=20)),
                ('year_of_reg', models.IntegerField()),
                ('passing', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=100, null=True)),
                ('daily_rate', models.IntegerField()),
                ('isactive', models.IntegerField()),
            ],
            options={
                'db_table': 'bikerent_bikedetail',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
