"""Defines all the functions related to the database"""
from app import Task
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table
    Returns:
        A list of dictionaries
    """
    
    query_results = Task.query.all()
    todo_list = []
    for result in query_results:
        item = {
            "id": result.id,
            "task": result.task,
            "status": result.status
        }
        todo_list.append(item)

    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`
    Args:
        task_id (int): Targeted task_id
        text (str): Updated description
    Returns:
        None
    """

    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    print(query)
    task = Task.query.get(task_id)
    if text!= task.task:
        task.task = text
    db.session.commit()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`
    Args:
        task_id (int): Targeted task_id
        text (str): Updated status
    Returns:
        None
    """

    
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    print(query)
    task = Task.query.get(task_id)
    if text!= task.status:
        task.status = text
    db.session.commit()

def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.
    Args:
        text (str): Task description
    Returns: The task ID for the inserted entry
    """
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(text, "Todo")
    print(query)
    task = Task(text)
    db.session.add(task)
    db.session.commit()
    descending = Task.query.order_by(Task.id.desc())
    last_item = descending.first()
    task_id = last_item.id
    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    query = 'Delete From tasks where id={};'.format(task_id)
    print(query)
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()