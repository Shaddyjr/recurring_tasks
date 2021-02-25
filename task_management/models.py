from django.db import models
from task_management.utils import TaskTerm, TaskStatus
# Create your models here.

class TaskPeriod(models.Model):
    # 1|daily|Every day|0 8 * * *
    # 2|weekly|Every week|0 0 * * 0
    # 3|monthly|Every month|0 0 1 * *
    # 4|quarterly|Every quarter|0 0 1 */3 *
    # 5|yearly|Every year|0 0 1 1 *
    period=models.CharField(max_length=16, primary_key=True)
    cron_string=models.CharField(blank=False, null=False, max_length=32)

class Task(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    due_date = models.DateField()
    note = models.CharField(blank=True, null=True, max_length=255)
    term = models.IntegerField(blank=True, null=True, default=TaskTerm.short, choices=TaskTerm.choices)
    recurring_period = models.ForeignKey(
        TaskPeriod,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    status = models.CharField(blank=False, null=False, default=TaskStatus.ideation, choices=TaskStatus.choices, max_length=16)

    @property
    def is_recurring(self):
        return self.recurring_period is not None