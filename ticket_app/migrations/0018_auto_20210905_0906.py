# Generated by Django 3.2.7 on 2021-09-05 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0017_alter_ticket_date_resolve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='department_assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_app.department'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priorytet',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('ASAP', 'ASAP')], default=1, max_length=64),
        ),
    ]
