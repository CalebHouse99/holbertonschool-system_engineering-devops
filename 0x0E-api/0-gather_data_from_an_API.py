#!/usr/bin/python3
"""returns information about employee list progress"""
import requests
from sys import argv


if __name__ == "__main__":
    #employee info
    emp = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    ).json()

    #employee todo list
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    ).json()

    #convert to list obj
    todo_list = [
        task.get("title") for task in todos if task.get("completed") is True
    ]

    #format and print
    print(
        "Employee {} is done with tasks({}/{}):".format(
            emp.get("name"), len(todo_list), len(todos)
        ), *todo_list, sep="\n\t "
    )