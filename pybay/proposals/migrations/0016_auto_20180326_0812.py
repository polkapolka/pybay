# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-03-26 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0015_auto_20180325_0015'),
    ]

    operations = [
        migrations.RunSQL(
            sql = "ALTER TABLE `proposals_talkproposal` ADD `what_will_attendees_learn` longtext;",
            reverse_sql = "ALTER TABLE `proposals_talkproposal` ADD `what_attendees_will_learn` longtext;"
        ),
    ]
