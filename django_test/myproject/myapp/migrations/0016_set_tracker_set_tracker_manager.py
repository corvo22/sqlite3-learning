# Generated by Django 4.2.2 on 2023-08-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_collection_table_entry_ratio'),
    ]

    operations = [
        migrations.CreateModel(
            name='set_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('owned', models.IntegerField(default=0)),
                ('ratio', models.CharField(max_length=64)),
                ('setcode', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='set_tracker_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
