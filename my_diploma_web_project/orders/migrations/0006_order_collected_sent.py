# Generated by Django 4.2.6 on 2023-12-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_collected_sent_order_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='collected_sent',
            field=models.BooleanField(default=False),
        ),
    ]
