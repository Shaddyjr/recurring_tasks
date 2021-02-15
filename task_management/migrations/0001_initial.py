# Generated by Django 3.1.6 on 2021-02-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('term', models.IntegerField(blank=True, choices=[(1, 'Short'), (2, 'Medium'), (3, 'Long')], default=1, null=True)),
                ('recurring_period', models.CharField(blank=True, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('annually', 'Annually')], max_length=16, null=True)),
                ('status', models.CharField(choices=[('ideation', 'Ideation'), ('in_progress', 'In Progress'), ('done', 'Done'), ('stuck', 'Stuck'), ('recurring', 'Recurring')], default='ideation', max_length=16)),
            ],
        ),
    ]
