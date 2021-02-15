import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recurringTasks.settings')
django.setup()

### Recurring Tasks ###
from task_management.models import Task
