#!/usr/bin/python3
"""Export an employee's TODO tasks to a JSON file."""

import json
import requests
import sys


def main():
    """Retrieve employee tasks and export them to JSON."""
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(
        "{}/users/{}".format(base_url, employee_id)
    )
    user = user_response.json()
    username = user.get("username")

    tasks_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    tasks = tasks_response.json()

    employee_tasks = []

    for task in tasks:
        employee_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {
        str(employee_id): employee_tasks
    }

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
