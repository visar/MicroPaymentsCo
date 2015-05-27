# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micropayments', '0002_auto_20150527_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaksioni',
            old_name='marresi',
            new_name='merr',
        ),
    ]
