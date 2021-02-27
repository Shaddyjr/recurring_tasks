from task_management.services.task_management_service import TaskManagementService
from task_management.utils import TaskTerm

class TaskManagementAPI():
    TERM_MAPPING = {val:word.capitalize() for val, word in TaskTerm.choices}

    def _format_task_output(self, task):
        return {
            "id": task.id,
            "title": task.title,
            "due_date": task.due_date,
            "note": task.note,
            "term": self._determine_term(task.term),
            "period": self._determine_period(task.recurring_period),
            "status": task.status,
        }

    def _determine_period(self, task_period):
        if task_period is not None:
            return task_period.period

    def _determine_term(self, task_term):
        if task_term is not None:
            return self.TERM_MAPPING[task_term]

    def create_task(self, title, due_date, note=None, term=None, period=None, status=None):
        TaskManagementService().create_task(title, due_date, note=note, term=term, period=period, status=status)
    
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
        tasks = TaskManagementService().get_done_tasks()
        return [self._format_task_output(task) for task in tasks]
    