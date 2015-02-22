# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='header',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
    ]
