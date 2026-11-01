#!/usr/bin/python3
"""Export all employees' TODO tasks to a JSON file."""

import json
import requests


def main():
    """Fetch all employees and their tasks and export them to JSON."""
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(base_url))
    users = users_response.json()

    tasks_response = requests.get("{}/todos".format(base_url))
    tasks = tasks_response.json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = []

        for task in tasks:
            if task.get("userId") == user_id:
                all_tasks[str(user_id)].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
