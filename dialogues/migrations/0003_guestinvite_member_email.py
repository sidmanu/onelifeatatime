# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialogues', '0002_guestinvite_homevisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestinvite',
            name='member_email',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
