# Expense Tracker

Expense Tracker is a simple command-line application to help you track your expenses and manage your balance. The project allows you to add, list, update, delete, and summarize your expenses. It uses a JSON file to store the data persistently.

Project - [project link](https://roadmap.sh/projects/expense-tracker)

## Features

- Add new expenses with description, amount, and type (credit or debit).
- List all expenses in a tabular format.
- Update existing expenses by ID.
- Delete expenses by ID.
- Summarize expenses for a specific month or year.
- Track your current balance.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

```sh
git clone https://github.com/Sajal-26/ExpenseTracker.git
cd ExpenseTracker
```

2. Add the batch file to your environment variables for easier access. The batch file `exp-cli.bat` contains:

```bat
@echo off
python path\to\your\ExpenseTracker\exp-cli.py %*
```

Replace `path\to\your\ExpenseTracker` with the actual path to your `ExpenseTracker` directory.

### Usage

You can use the command-line interface to interact with the Expense Tracker. The following commands are supported:

1. **Add an expense:**

```sh
exp-cli add --desc "Grocery Shopping" --amt 1500 -t d
```

2. **List all expenses:**

```sh
exp-cli list
```

3. **Update an expense:**

```sh
exp-cli update --id 1 --desc "Updated Description" --amt 2000
```

4. **Delete an expense:**

```sh
exp-cli delete --id 1
```

5. **Summarize expenses:**

```sh
exp-cli summary -m 11 -y 2023
```

### Commands and Arguments

- `add`: Add a new expense.
  - `--desc`: Description of the expense (required).
  - `--amt`: Amount of the expense (required).
  - `-t`: Type of the expense, 'c' for credit, 'd' for debit (required).

- `list`: List all expenses.

- `update`: Update an existing expense.
  - `--id`: ID of the expense to update (required).
  - `--desc`: Updated description (optional).
  - `--amt`: Updated amount (optional).

- `delete`: Delete an expense.
  - `--id`: ID of the expense to delete (required).

- `summary`: Summarize expenses for a specific month and/or year.
  - `-m`: Month (optional).
  - `-y`: Year (optional).

### Example

```sh
exp-cli add --desc "Dinner at restaurant" --amt 2000 -t d
exp-cli list
exp-cli update --id 1 --desc "Dinner at fancy restaurant"
exp-cli delete --id 1
exp-cli summary -m 11 -y 2023
```
