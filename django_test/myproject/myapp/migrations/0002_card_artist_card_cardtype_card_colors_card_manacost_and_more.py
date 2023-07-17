# Generated by Django 4.2.2 on 2023-07-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='artist',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='cardType',
            field=models.CharField(default='card', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='colors',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='manaCost',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='power',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='setNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='setcode',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='subtypes',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='supertypes',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='text',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='toughness',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
