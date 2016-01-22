# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_name', models.CharField(max_length=60)),
                ('friend_name', models.CharField(max_length=60)),
                ('member_email', models.CharField(max_length=60)),
                ('dialogue_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(unique=True, max_length=60)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('leader', models.ForeignKey(to='dialogues.Leader', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('leader', models.ForeignKey(to='dialogues.Leader', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='region',
            name='parent',
            field=models.ForeignKey(to='dialogues.Zone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='leader',
            field=models.ForeignKey(to='dialogues.Leader', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='parent',
            field=models.ForeignKey(to='dialogues.Chapter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dialogue',
            name='district',
            field=models.ForeignKey(to='dialogues.District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chapter',
            name='leader',
            field=models.ForeignKey(to='dialogues.Leader', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chapter',
            name='parent',
            field=models.ForeignKey(to='dialogues.Region'),
            preserve_default=True,
        ),
    ]
