# ALU Back-End

## API

This project demonstrates how to gather data from a REST API and export employee TODO list information in different formats.

### Tasks

**0. Gather data from an API**

Retrieves an employee's information and displays their completed TODO tasks and total task progress.

**1. Export to CSV**

Exports all TODO tasks belonging to a specific employee into a CSV file.

**2. Export to JSON**

Exports all TODO tasks belonging to a specific employee into a JSON file.

**3. Dictionary of list of dictionaries**

Exports all employees' TODO tasks into one JSON file.

### Requirements

- Python 3
- Requests library

### Usage

Navigate to the `api` directory:

```bash
cd api
```

Run the scripts using:

```bash
python3 0-gather_data_from_an_API.py 2
python3 1-export_to_CSV.py 2
python3 2-export_to_JSON.py 2
python3 3-dictionary_of_list_of_dictionaries.py
```

### API

The project uses the JSONPlaceholder REST API:

https://jsonplaceholder.typicode.com

### Author

Liliose Gashugi Muhimpundu
