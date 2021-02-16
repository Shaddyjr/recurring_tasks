from task_management.models import Task, TaskPeriod

class TaskManagementService():
    def __init__(self):
        pass

    def create_task(self, title, due_date, note=None, term=None, period=None):
        Task.objects.create(
            title = title,
            due_date = due_date,
            note = note,
            term = term,
            recurring_period = self._get_task_period(period),
        )

    def _get_task(self, task_id):
        return Task.objects.get(id=task_id)
    
    def delete_task(self, task_id):
        self._get_task(task_id).delete()
    
    def update_task(self, task_id, **kwargs):
        task_fields = [
            "title",
            "due_date",
            "note",
            "term",
            "period",
            "status",   
        ]

        task = self._get_task(task_id)
        keys = kwargs.keys()
        for task_field in task_fields:
            if task_field in keys:
                setattr(task, task_field, kwargs.get(task_fields))
    
    def _get_task_period(self, period):
        if period:
            return TaskPeriod.objects.get(period=period)