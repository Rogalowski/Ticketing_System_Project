# Generated by Django 3.2.7 on 2021-09-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0016_alter_ticket_date_resolve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_resolve',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
