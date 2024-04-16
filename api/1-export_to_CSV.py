#!/usr/bin/python3
"""collecting data from API"""
import csv
import requests
import sys


def todo_list(employee_id):
    """
    This function will fetch the URL, user info,
    TODO list and display the employee progress
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # User info
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    user_id = user_data['id']
    username = user_data['username']

    # getting TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # task progress
    total_task = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    # display progress
    print_value = 'Employee {} is done with tasks({}/{}):'\
        .format(username, done_tasks, total_task)
    print(print_value)
    for todo in todos_data:
        if todo['completed']:
            print(f'\t{todo["title"]}')

    # Export data to CSV
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['USER_ID', 'USERNAME',
                            'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in todos_data:
            csvwriter.writerow([user_id, username,
                                todo['completed'], todo['title']])

    print(f'Data exported to {filename}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    todo_list(employee_id)
