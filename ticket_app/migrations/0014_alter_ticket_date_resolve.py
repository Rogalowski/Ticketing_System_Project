# Generated by Django 3.2.7 on 2021-09-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0013_alter_ticket_date_resolve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_resolve',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
