# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_respuc', '0005_auto_20170203_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituicao',
            old_name='email',
            new_name='email_instituicao',
        ),
    ]
