# Generated by Django 4.2.2 on 2023-07-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cardmanager_rename_cardtype_card_types_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardManager',
        ),
        migrations.AlterField(
            model_name='card',
            name='power',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.IntegerField(null=True),
        ),
    ]
