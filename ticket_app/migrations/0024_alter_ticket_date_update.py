# Generated by Django 3.2.7 on 2021-09-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0023_alter_ticket_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
