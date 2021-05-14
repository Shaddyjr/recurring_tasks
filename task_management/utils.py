from django.db import models

class TaskStatus(models.TextChoices):
    ideation = 'ideation', 'Ideation'
    in_progress = 'in_progress', 'In Progress'
    done = 'done', 'Done'
    blocked = 'blocked', 'Blocked'
    past_due = 'past_due', 'Past Due'
