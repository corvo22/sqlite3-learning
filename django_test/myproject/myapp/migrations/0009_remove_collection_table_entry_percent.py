# Generated by Django 4.2.2 on 2023-07-24 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_collection_table_entry_percent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection_table_entry',
            name='percent',
        ),
    ]
