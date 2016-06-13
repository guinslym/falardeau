# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='expiring_date',
            field=models.DateField(null=True, help_text='release date', default=datetime.datetime(2016, 7, 13, 22, 25, 18, 795481, tzinfo=utc), blank=True),
        ),
    ]
