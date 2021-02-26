import datetime
from task_management.models import Task, TaskPeriod, TaskTerm, TaskStatus
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
        past_due_tasks = Task.objects.exclude(status__in = [TaskStatus.done, TaskStatus.blocked]).filter(due_date__lt=today)

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
        if isinstance(date, datetime.date):
            return date
        return parse(date).date()

    def create_task(self, title, due_date, note=None, term=None, period=None, status=None):
        Task.objects.create(
            title = title,
            due_date = self.parse_date(due_date),
            note = note,
            term = self._get_task_term(term),
            recurring_period = self._get_task_period(period),
            status = status,
        )

    def get_task(self, task_id):
        return Task.objects.get(id=task_id)
    
    def delete_task(self, task_id):
        self.get_task(task_id).delete()
    
    def update_task(self, task_id, **kwargs):
        task_fields = [
            "title",
            "due_date",
            "note",
            "term",
            "period",
            "status",
        ]

        task = self.get_task(task_id)
        keys = kwargs.keys()
        for task_field in task_fields:
            if task_field in keys:
                setattr(task, task_field, kwargs.get(task_field))
        task.save()

    def _get_task_term(self, term):
        if term:
            return getattr(TaskTerm, term.lower())

    def _get_task_period(self, period):
        if period:
            return TaskPeriod.objects.get(period=period)

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
        task.due_date = next_due_date
        task.save()

    def get_tasks_for_today(self):
        today = datetime.datetime.now().date()
        return Task.objects.filter(due_date = today)
    
    def get_live_tasks(self):
        return Task.objects.exclude(status = TaskStatus.done)

    def get_done_tasks(self):
        return Task.objects.filter(status = TaskStatus.done)

    # TODO
    def get_overdue_tasks(self):
        pass

    # TODO
    def get_tasks_for_date(self):
        pass