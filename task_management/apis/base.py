from task_management.services.task_management_service import TaskManagementService

class TaskManagementAPI():
    def _format_task_output(self, task):
        return {
            "id": task.id,
            "title": task.title,
            "due_date": task.due_date,
            "note": task.note,
            "term": task.term,
            "period": self._determine_period(task.recurring_period),
            "status": task.status,
        }

    def _determine_period(self, task_period):
        if task_period:
            return task_period.period

    def create_task(self, title, due_date, note=None, term=None, period=None):
        TaskManagementService().create_task(title, due_date, note=None, term=None, period=None)
    
    def get_task(self, task_id):
        task = TaskManagementService().get_task(task_id)
        return self._format_task_output(task)

    def delete_task(self, task_id):
        TaskManagementService().delete_task(task_id)
    
    def update_task(self, task_id, **kwargs):
        TaskManagementService().update_task(task_id, **kwargs)
    
    def complete_task(self, task_id):
        TaskManagementService().complete_task(task_id)
    
    def get_tasks_for_today(self):
        tasks = TaskManagementService().get_tasks_for_today()
        return [self._format_task_output(task) for task in tasks]

    def get_live_tasks(self):
        tasks = TaskManagementService().get_live_tasks()
        return [self._format_task_output(task) for task in tasks]

    def get_done_tasks(self):
        tasks = TaskManagementService().get_done_tasks(term)
        return [self._format_task_output(task) for task in tasks]
    