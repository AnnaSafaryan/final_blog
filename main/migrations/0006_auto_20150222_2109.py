# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150222_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
