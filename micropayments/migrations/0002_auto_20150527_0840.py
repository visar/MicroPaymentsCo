# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micropayments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filiala',
            name='bashkepunon',
            field=models.ManyToManyField(blank=True, to='micropayments.Klienti'),
        ),
    ]
