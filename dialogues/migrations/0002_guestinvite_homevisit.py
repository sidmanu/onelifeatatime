# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialogues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestInvite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friend_name', models.CharField(max_length=30)),
                ('member_name', models.CharField(max_length=30)),
                ('invite_date', models.DateField()),
                ('info', models.TextField(blank=True)),
                ('district', models.ForeignKey(to='dialogues.District')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomeVisit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visitor_name', models.CharField(max_length=30)),
                ('visited_name', models.CharField(max_length=30)),
                ('visitor_email', models.CharField(max_length=30)),
                ('visit_date', models.DateField()),
                ('district', models.ForeignKey(to='dialogues.District')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
