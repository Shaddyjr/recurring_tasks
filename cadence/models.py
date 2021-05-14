from django.db import models

class Cadence(models.Model):
    period=models.CharField(max_length=16, primary_key=True)
    cron_string=models.CharField(blank=False, null=False, max_length=32)
