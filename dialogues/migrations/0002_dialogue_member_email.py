# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialogues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialogue',
            name='member_email',
            field=models.CharField(default='dummy@dummy.com', unique=True, max_length=60),
            preserve_default=False,
        ),
    ]
