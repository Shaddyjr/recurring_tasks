# Generated by Django 3.1.6 on 2021-03-21 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0007_auto_20210306_2155'),
        ('contact_management', '0003_default_foreignkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurringcontact',
            name='preferred_cadence',
            field=models.ForeignKey(blank=True, default='yearly', null=True, on_delete=django.db.models.deletion.PROTECT, to='task_management.taskperiod'),
        ),
    ]
