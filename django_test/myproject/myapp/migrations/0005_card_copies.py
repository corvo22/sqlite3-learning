# Generated by Django 4.2.2 on 2023-07-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_cardmanager_alter_card_power_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='copies',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
