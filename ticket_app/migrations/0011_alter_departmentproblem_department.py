# Generated by Django 3.2.7 on 2021-09-04 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0010_auto_20210904_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentproblem',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_app.department'),
        ),
    ]
