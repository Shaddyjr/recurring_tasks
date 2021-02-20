from task_management.models import Task, TaskPeriod
from datetime import datetime
from croniter import croniter

class TaskManagementService():
    def __init__(self):
        pass

    def create_task(self, title, due_date, note=None, term=None, period=None):
        Task.objects.create(
            title = title,
            due_date = due_date,
            note = note,
            term = term,
            recurring_period = self.get_task_period(period),
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
                setattr(task, task_field, kwargs.get(task_fields))
    
    def get_task_period(self, period):
        if period:
            return TaskPeriod.objects.get(period=period)

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        # Recurring tasks don't truly ever complete
        if task.recurring_period is not None:
            self._get_new_due_date_for_recurring(task)
        else:
            self.update_task(
                task_id = task.id,
                status = Task.TaskStatus.done
            )

    def _set_new_due_date_for_recurring(self, task):
        cron = croniter(task.recurring_period.cron_string)
        next_due_date = cron.get_next(datetime).date()
        task.due_date = next_due_date

    def get_tasks_for_today(self):
        today = datetime.now().date()
        return Task.objects.filter(due_date = today)
    
    def get_live_tasks_by_term(self, term):
        '''
        Parameters:
            `term` (int): 1 => short, 2 => medium, 3 => long
        '''
        return Task.objects.exclude(status = Task.TaskStatus.done).filter(term = term)
        

    def get_tasks_by_status(self, status):
        return Task.objects.filter(status = status)
