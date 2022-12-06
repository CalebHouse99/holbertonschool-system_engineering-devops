#!/usr/bin/python3
"""Export in JSON format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]

    todo_response = requests.get('https://jsonplaceholder.typicode.com/todos/\
?userId={}'.format(user_id))

    user_response = requests.get('https://jsonplaceholder.typicode.com/users/\
{}'.format(user_id))

    todo_data = todo_response.text
    parse_todo = json.loads(todo_data)

    user_data = user_response.text
    parse_user = json.loads(user_data)

    user_name = parse_user['name']
    completed_tasks = 0
    total_tasks = 0

    for task in parse_todo:
        total_tasks += 1
        if task['completed']:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):\
    ".format(user_name, completed_tasks, total_tasks))

    for task in parse_todo:
        if task['completed']:
            print("\t {}\n".format(task['title']), end="")
