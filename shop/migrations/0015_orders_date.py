# Generated by Django 4.1.7 on 2023-07-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
