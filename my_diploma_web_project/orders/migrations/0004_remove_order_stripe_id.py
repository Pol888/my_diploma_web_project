# Generated by Django 4.2.6 on 2023-12-07 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_collected_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='stripe_id',
        ),
    ]