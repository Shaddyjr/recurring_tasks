from django.db import models
from task_management.models import TaskPeriod
from model_helpers import TimeStampMixin
from task_management.utils import TaskPeriodTypes

YOU = 'you'
DEFAULT_TASK_PERIOD = TaskPeriodTypes.yearly.name

class RecurringContact(TimeStampMixin):
    first_name = models.CharField(blank=False, null=False, max_length=32)
    last_name = models.CharField(blank=False, null=False, max_length=32)
    preferred_cadence = models.ForeignKey(
        TaskPeriod,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        default=DEFAULT_TASK_PERIOD,
    )

class ContactInteraction(TimeStampMixin):
    contact = models.ForeignKey(
        RecurringContact,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    # 0 = you initiated, 1 = they initiated
    direction = models.BooleanField(blank=False, null=False)
    prev_interaction = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    @property
    def initiator(self):
        # 0 = you initiated, 1 = they initiated
        if self.direction:
            return f"{self.contact.first_name} {self.contact.last_name}"
        return YOU

    @property
    def time_since_last_interaction(self):
        return self.created_at - self.prev_interaction.created_at
