# Generated by Django 4.1.1 on 2022-11-03 12:43

import django.contrib.postgres.fields
import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_alter_player_saved_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='saved_players',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.citext.CITextField(max_length=100), default=list, size=None),
        ),
    ]