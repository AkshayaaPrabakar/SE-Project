# Generated by Django 5.1.6 on 2025-04-03 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='monthly_target',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
