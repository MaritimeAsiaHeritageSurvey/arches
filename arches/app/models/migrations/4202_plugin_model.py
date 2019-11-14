# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-18 13:20


import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("models", "3892_integrity_error"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plugin",
            fields=[
                ("pluginid", models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("icon", models.TextField(default=None)),
                ("component", models.TextField()),
                ("componentname", models.TextField()),
                ("config", django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column="config", null=True)),
            ],
            options={"db_table": "plugins", "managed": True},
        ),
    ]
