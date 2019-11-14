# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-17 12:36


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("models", "4771_searchcomponent"),
    ]

    operations = [
        migrations.AddField(model_name="maplayer", name="legend", field=models.TextField(blank=True, null=True)),
        migrations.RunSQL(
            sql="""
            UPDATE d_data_types
            SET defaultconfig = jsonb_build_object('layerLegend', '') || COALESCE(defaultconfig, '{}'::jsonb)
            WHERE datatype = 'geojson-feature-collection';

            UPDATE nodes
            SET config = COALESCE(config, '{}'::jsonb) || jsonb_build_object('layerLegend', '')
            WHERE datatype = 'geojson-feature-collection';
            """,
            reverse_sql="""
            UPDATE d_data_types
            SET defaultconfig = defaultconfig - 'layerLegend'
            WHERE datatype = 'geojson-feature-collection';

            UPDATE nodes
            SET config = config - 'layerLegend'
            WHERE datatype = 'geojson-feature-collection';
            """,
        ),
    ]
