# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialogues', '0002_dialogue_member_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialogue',
            name='member_email',
            field=models.CharField(max_length=60),
        ),
    ]
