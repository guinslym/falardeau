# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20160614_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='expiring_date',
            field=models.DateField(null=True, help_text='release date', default=datetime.datetime(2016, 7, 14, 22, 7, 7, 898212, tzinfo=utc), blank=True),
        ),
    ]
