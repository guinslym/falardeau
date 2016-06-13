# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django_extensions.db.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, null=True, max_length=12, unique=True)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='film/%Y/%m/%d')),
                ('expiring_date', models.DateField(default=datetime.datetime(2016, 7, 13, 22, 8, 20, 476551, tzinfo=utc), blank=True, null=True, help_text='release date')),
            ],
            options={
                'get_latest_by': 'modified',
                'ordering': ('-modified', '-created'),
                'abstract': False,
            },
        ),
    ]
