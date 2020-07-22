import pytest
import os

def test_add_task():
    assert os.system("python3 mark thehill") == 0, "Failed add task"


def test_add_task_subtask():
    assert os.system("python3 mark gdc") == 0, "Failed add sub task"


def test_log_exists():
    assert os.path.isfile("history.log"), "No history log"
