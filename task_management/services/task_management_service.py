import datetime
from task_management.models import Task, TaskPeriod, TaskStatus
from croniter import croniter
from dateutil.parser import parse

class TaskManagementService():
    def __init__(self):
        self.process_tasks()

    def process_tasks(self):
        """
        Syncs tasks to the moment the service is invoked (not using a cron job or server to upkeep).
        """
        today = datetime.datetime.now().date()
        past_due_tasks = self.get_live_tasks().filter(due_date__lt=today)

        for task in past_due_tasks:
            # recurring set to next due date
            if task.is_recurring:
                self._set_new_due_date_for_recurring(task)
            # past due assigned status = "past_due"
            else:
                self.update_task(
                    task_id = task.id,
                    status = TaskStatus.past_due
                )
  
    def parse_date(self, date):
        if not date:
            return  datetime.datetime.now().date()
        if isinstance(date, datetime.date):
            return date
        return parse(date).date()

    def create_task(self, title, due_date, note=None, period=None, status=None):
        Task.objects.create(
            title = title,
            due_date = self.parse_date(due_date),
            note = note,
            recurring_period = self._get_task_period(period),
            status = self._get_task_status(status),
        )

    def get_task(self, task_id):
        return Task.objects.get(id=task_id)
    
    def delete_task(self, task_id):
        self.get_task(task_id).delete()
    
    def update_task(self, task_id, **kwargs):
        task_fields = [
            ("title", None),
            ("due_date", self.parse_date),
            ("note", None),
            ("period", self._get_task_period),
            ("status", self._get_task_status),
        ]

        task = self.get_task(task_id)
        keys = kwargs.keys()
        for task_field, func in task_fields:
            if task_field in keys:
                val = kwargs.get(task_field)
                if func:
                    val = func(val)
                setattr(task, task_field, val)
        task.save()

    def _get_task_period(self, period):
        if period is not None:
            return TaskPeriod.objects.get(period=period.lower())

    def _get_task_status(self, status):
        return getattr(TaskStatus, status.lower())

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        # Recurring tasks don't truly ever complete
        if task.is_recurring:
            self._set_new_due_date_for_recurring(task)
        else:
            self.update_task(
                task_id = task.id,
                status = TaskStatus.done
            )

    def _set_new_due_date_for_recurring(self, task):
        cron = croniter(task.recurring_period.cron_string)
        next_due_date = cron.get_next(datetime.datetime).date()
        self.update_task(
            task_id = task.id,
            due_date = next_due_date,
            status = TaskStatus.ideation,
        )

    def get_tasks_for_today(self):
        today = datetime.datetime.now().date()
        return self.get_live_tasks().filter(due_date = today)
    
    def get_live_tasks(self):
        return Task.objects.filter(status__in = [TaskStatus.ideation, TaskStatus.in_progress])

    def get_done_tasks(self):
        return Task.objects.filter(status = TaskStatus.done)

    # TODO
    def get_overdue_tasks(self):
        pass

    # TODO
    def get_tasks_for_date(self):
        pass