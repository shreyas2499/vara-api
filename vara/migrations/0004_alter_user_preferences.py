# Generated by Django 4.2.11 on 2024-04-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vara', '0003_monthlyconsumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=models.JSONField(blank=True),
        ),
    ]