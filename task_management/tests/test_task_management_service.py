import pytest
from task_management.services.task_management_service import (
    TaskManagementService, Task, TaskPeriod, TaskStatus
)

# https://github.com/pytest-dev/pytest-mock
class TestTaskManagementService():
    @pytest.fixture
    def task(self):


    def test_create_task(self):
        assert False

    def test_get_task(self):
        pass

    def test_delete_task(self):
        pass

    def test_update_task(self):
        pass

    def test_complete_task(self):
        pass

    def test_get_tasks_for_today(self):
        pass

    def test_get_live_tasks(self):
        pass

    def test_get_done_tasks(self):
        pass
