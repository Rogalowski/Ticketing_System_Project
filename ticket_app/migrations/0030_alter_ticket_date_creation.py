# Generated by Django 3.2.7 on 2021-09-06 09:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0029_alter_ticket_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_creation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 6, 9, 54, 1, 566871, tzinfo=utc)),
        ),
    ]
