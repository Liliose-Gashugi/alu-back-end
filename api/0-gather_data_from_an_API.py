#!/usr/bin/python3
"""Gather data from an API and display an employee's TODO progress."""

import requests
import sys


def main():
    """Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    employee_response = requests.get(
        "{}/users/{}".format(base_url, employee_id)
    )
    employee = employee_response.json()

    tasks_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    tasks = tasks_response.json()

    employee_name = employee.get("name")
    completed_tasks = [
        task for task in tasks if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), len(tasks)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
