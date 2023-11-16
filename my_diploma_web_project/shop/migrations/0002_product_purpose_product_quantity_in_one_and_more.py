# Generated by Django 4.2.6 on 2023-11-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='purpose',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_in_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(default='', max_length=200),
        ),
    ]