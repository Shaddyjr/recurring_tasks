from django.db import models
from task_management.utils import TaskStatus
from model_helpers import TimeStampMixin
from cadence.models import Cadence
 
class Task(TimeStampMixin):
    title = models.CharField(blank=False, null=False, max_length=100)
    due_date = models.DateField()
    note = models.CharField(blank=True, null=True, max_length=255)
    recurring_period = models.ForeignKey(
        Cadence,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    status = models.CharField(blank=False, null=False, default=TaskStatus.ideation, choices=TaskStatus.choices, max_length=16)

    @property
    def is_recurring(self):
        return self.recurring_period is not None