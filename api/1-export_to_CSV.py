#!/usr/bin/python3
"""Export an employee's TODO tasks to a CSV file."""

import csv
import requests
import sys


def main():
    """Retrieve employee tasks and export them to CSV."""
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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
