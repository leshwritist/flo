# Generated by Django 5.1.1 on 2024-10-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flo', '0006_company_notification_threshold_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Amount_paid',
            new_name='amount_paid',
        ),
    ]
