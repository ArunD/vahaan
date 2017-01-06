# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikerent', '0002_auto_20150104_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='creator',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
