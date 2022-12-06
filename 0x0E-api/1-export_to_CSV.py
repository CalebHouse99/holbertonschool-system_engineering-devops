#!/usr/bin/python3
"""Export in CSV format"""
import csv
import requests
import sys


def export_to_CSV():
    """stores into CSV file"""
    n = sys.argv[1]

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(n)
    url_tasks = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(n))

    tasks = requests.get(url_tasks).json()
    user_info = requests.get(url_user).json()
    employee_name = user_info.get("username")

    with open('{}.csv'.format(n), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([task.get('userId'), employee_name,
                             task.get('completed'), task.get('title')])


if __name__ == '__main__':
    export_to_CSV()
