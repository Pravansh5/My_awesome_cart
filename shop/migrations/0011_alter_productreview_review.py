# Generated by Django 4.1.7 on 2023-06-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
