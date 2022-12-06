#!/usr/bin/python3
"""Export to JSON format"""
import json
import requests


def everyone_todo_to_JSON():
    """saves in JSON format"""
    url = "https://jsonplaceholder.typicode.com/"

    employee_names = requests.get(url + 'users').json()
    employees_todos = requests.get(url + 'todos').json()

    return_dict = {}
    all_users_dict = {}

    for employee in employee_names:
        user_id = employee.get('id')
        return_dict[user_id] = []
        all_users_dict[user_id] = employee.get('username')

    for task in employees_todos:
        employee_tasks_dict = {}
        user_id = task.get('userId')
        employee_tasks_dict['username'] = all_users_dict.get(user_id)
        employee_tasks_dict['task'] = task.get('title')
        employee_tasks_dict['completed'] = task.get('completed')
        return_dict.get(user_id).append(employee_tasks_dict)

    with open('todo_all_employees.json', 'w') as JSONFile:
        json.dump(return_dict, JSONFile)


if __name__ == "__main__":
    everyone_todo_to_JSON()
