from django.db import models

# Create your models here.
class Task(models.Model):
    class TaskTerm(models.IntegerChoices):
        short = 1
        medium = 2
        long = 3
    
    class TaskPeriod(models.TextChoices):
        daily = 'daily', 'Daily'
        weekly = 'weekly', 'Weekly'
        monthly = 'monthly', 'Monthly'
        quarterly = 'quarterly', 'Quarterly'
        annually = 'annually', 'Annually'

    class TaskStatus(models.TextChoices):
        ideation = 'ideation', 'Ideation'
        in_progress = 'in_progress', 'In Progress'
        done = 'done', 'Done'
        stuck = 'stuck', 'Stuck'
        recurring = 'recurring', 'Recurring'

    title = models.CharField(blank=False, null=False, max_length=100)
    due_date = models.DateField()
    notes = models.CharField(blank=True, null=True, max_length=255)
    term = models.IntegerField(blank=True, null=True, default=TaskTerm.short, choices=TaskTerm.choices)
    recurring_period = models.CharField(blank=True, null=True, choices=TaskPeriod.choices, max_length=16)
    status = models.CharField(blank=False, null=False, default=TaskStatus.ideation, choices=TaskStatus.choices, max_length=16)