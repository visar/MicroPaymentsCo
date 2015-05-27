# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filiala',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('adresa', models.CharField(max_length=200)),
                ('telefoni', models.CharField(max_length=200)),
                ('shuma', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Klienti',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('emri', models.CharField(max_length=200)),
                ('mbiemri', models.CharField(max_length=200)),
                ('telefoni', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Punetori',
            fields=[
                ('pusername', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True, serialize=False, primary_key=True)),
                ('emri', models.CharField(max_length=200)),
                ('mbiemri', models.CharField(max_length=200)),
                ('adresa', models.CharField(max_length=200)),
                ('telefoni', models.CharField(max_length=200)),
                ('fid', models.ForeignKey(to='micropayments.Filiala')),
            ],
        ),
        migrations.CreateModel(
            name='Transaksioni',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('deviza', models.CharField(max_length=10)),
                ('shuma', models.CharField(max_length=10)),
                ('provizioni', models.CharField(max_length=10)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('proceson', models.ForeignKey(to='micropayments.Punetori')),
            ],
        ),
        migrations.CreateModel(
            name='Derguesi',
            fields=[
                ('did', models.OneToOneField(to='micropayments.Klienti', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marresi',
            fields=[
                ('mid', models.OneToOneField(to='micropayments.Klienti', serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='filiala',
            name='bashkepunon',
            field=models.ManyToManyField(to='micropayments.Klienti'),
        ),
        migrations.AddField(
            model_name='transaksioni',
            name='dergon',
            field=models.ForeignKey(to='micropayments.Derguesi'),
        ),
        migrations.AddField(
            model_name='transaksioni',
            name='marresi',
            field=models.ForeignKey(to='micropayments.Marresi'),
        ),
    ]
