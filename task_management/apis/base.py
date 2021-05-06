from django.forms.models import model_to_dict
from task_management.services.task_management_service import TaskManagementService


class TaskManagementAPI():
    def _format_model_list(self, model_list):
        return [model_to_dict(model) for model in model_list]

    def create_task(self, title, due_date, note=None, period=None, status=None):
        TaskManagementService().create_task(
            title,
            due_date,
            note=note,
            period=period,
            status=status
        )

    def get_task(self, task_id):
        task = TaskManagementService().get_task(task_id)
        return model_to_dict(task)

    def delete_task(self, task_id):
        TaskManagementService().delete_task(task_id)

    def update_task(self, task_id, **kwargs):
        TaskManagementService().update_task(task_id, **kwargs)

    def complete_task(self, task_id):
        TaskManagementService().complete_task(task_id)

    def get_tasks_for_today(self):
        tasks = TaskManagementService().get_tasks_for_today()
        return self._format_model_list(tasks)

    def get_live_tasks(self):
        tasks = TaskManagementService().get_live_tasks()
        return self._format_model_list(tasks)

    def get_done_tasks(self):
        tasks = TaskManagementService().get_done_tasks()
        return self._format_model_list(tasks)
    