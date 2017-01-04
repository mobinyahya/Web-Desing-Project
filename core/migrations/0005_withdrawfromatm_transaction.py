# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_paymentorder_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawfromatm',
            name='transaction',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Transaction'),
            preserve_default=False,
        ),
    ]
