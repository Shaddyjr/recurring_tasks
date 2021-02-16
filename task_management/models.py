from django.db import models

# Create your models here.

class TaskPeriod(models.Model):
    # 1|daily|Every day|0 8 * * *
    # 2|weekly|Every week|0 0 * * 0
    # 3|monthly|Every month|0 0 1 * *
    # 4|quarter|Every quarter|0 0 1 */3 *
    # 5|yearly|Every year|0 0 1 1 *
    period=models.CharField(max_length=16, primary_key=True)
    note=models.CharField(blank=True, null=True, max_length=255)
    cron_string=models.CharField(blank=False, null=False, max_length=32)

class Task(models.Model):
    class TaskTerm(models.IntegerChoices):
        short = 1
        medium = 2
        long = 3

    class TaskStatus(models.TextChoices):
        ideation = 'ideation', 'Ideation'
        in_progress = 'in_progress', 'In Progress'
        done = 'done', 'Done'
        blocked = 'blocked', 'Blocked'
        recurring = 'recurring', 'Recurring'

    title = models.CharField(blank=False, null=False, max_length=100)
    due_date = models.DateField()
    note = models.CharField(blank=True, null=True, max_length=255)
    term = models.IntegerField(blank=True, null=True, default=TaskTerm.short, choices=TaskTerm.choices)
    recurring_period = models.ForeignKey(
        TaskPeriod,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    status = models.CharField(blank=False, null=False, default=TaskStatus.ideation, choices=TaskStatus.choices, max_length=16)
