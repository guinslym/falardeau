# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20160614_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='expiring_date',
            field=models.DateField(blank=True, null=True, help_text='release date', default=datetime.datetime(2016, 7, 15, 0, 6, 39, 368485, tzinfo=utc)),
        ),
    ]
