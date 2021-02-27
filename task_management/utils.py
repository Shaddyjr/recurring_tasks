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
    past_due = 'past_due', 'Past Due'

class TaskPeriodTypes(models.TextChoices):
    # https://crontab.guru/
    daily = '0 8 * * *'
    weekly = '0 0 * * 0'
    monthly = '0 0 1 * *'
    quarterly = '0 0 1 */3 *'
    yearly = '0 0 1 1 *'
    monday = '0 0 * * MON'
    tuesday = '0 0 * * TUE'
    wednesday = '0 0 * * WED'
    thursday = '0 0 * * THU'
    friday = '0 0 * * FRI'
    saturday = '0 0 * * SAT'
    sunday = '0 0 * * SUN'
