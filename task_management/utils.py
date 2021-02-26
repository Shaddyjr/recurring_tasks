from django.db import models

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
    past_due = 'past_due', 'Past Due'

class TaskPeriodTypes(models.TextChoices):
    daily = '0 8 * * *'
    weekly = '0 0 * * 0'
    monthly = '0 0 1 * *'
    quarterly = '0 0 1 */3 *'
    yearly = '0 0 1 1 *'
