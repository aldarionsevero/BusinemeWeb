# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pontuation',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
