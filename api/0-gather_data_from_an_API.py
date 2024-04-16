#!/usr/bin/python3
"""collecting data from API"""
import requests
import sys


def todo_list(employee_id):
    """
    this function will fetch the URL, user info,
    TODO list and display the employee progress
    """

    base_url = 'https://jsonplaceholder.typicode.com'

    """ User info """
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    """ getting TODO list """
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    """task progress"""
    total_task = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    """ display progress """
    print(f'Employee {employee_name} /
          is done with tasks({done_tasks} / {total_task}): ')
    for todo in todos_data:
        if todo['completed']:
            print(f'\t{todo["title"]}')


if __name__ == "__main__":
    """call the function"""

    if len(sys.argv) != 2:
        print("usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    todo_list(employee_id)
