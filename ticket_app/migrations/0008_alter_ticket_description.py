# Generated by Django 3.2.7 on 2021-09-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0007_auto_20210904_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]