# Generated by Django 4.1.7 on 2023-07-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_orders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='payment_mode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]