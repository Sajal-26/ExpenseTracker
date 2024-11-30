# ExpenseTracker

## Overview

ExpenseTracker is a command-line tool for managing personal expenses. It allows users to add, list, update, delete, and summarize expenses, all stored in a JSON file for persistence. This program provides an easy way to keep track of your spending directly from the terminal.

Project - [project link](https://roadmap.sh/projects/expense-tracker)

## Features

- **Add Expense:** Add a new expense with a description and amount.
- **List Expenses:** List all recorded expenses.
- **Update Expense:** Update the description or amount of an existing expense by ID.
- **Delete Expense:** Delete an expense by ID.
- **Summarize Expenses:** Calculate and display the total expenses for a specific month and year.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sajal-26/ExpenseTracker.git
    cd ExpenseTracker
    ```

2. **Ensure you have Python installed:**
    - You can download Python from [python.org](https://www.python.org/downloads/).

3. **Add the batch file to your environment variables:**
    - Create a batch file named `exp-cli.bat` with the following content:
      ```bat
      @echo off
      pythonpPath\to\ExpenseTracker\exp-cli.py %*
      ```
    - Add the path to `exp-cli.bat` to your system's environment variables.

## Usage

Run the `exp-cli` command followed by the desired action and necessary parameters:

### Commands

- **Add an Expense:**
    ```bash
    exp-cli add --desc "Description of the expense" --amt 123.45
    ```

- **List all Expenses:**
    ```bash
    exp-cli list
    ```

- **Update an Expense:**
    ```bash
    exp-cli update --id 1 --desc "Updated description" --amt 543.21
    ```

- **Delete an Expense:**
    ```bash
    exp-cli delete --id 1
    ```

- **Summarize Expenses:**
    ```bash
    exp-cli summary -m 11 -y 2023
    ```

### Arguments

- `command`: The action to perform (add, list, update, delete, summary).
- `--desc`: Description of the expense (required for add and update).
- `--amt`: Amount of the expense (required for add and update).
- `--id`: ID of the expense (required for update and delete).
- `-m`: Month for filtering expenses in the summary.
- `-y`: Year for filtering expenses in the summary.

## Example

Add a new expense:
```bash
exp-cli add --desc "Groceries" --amt 150.00
```

List all expenses:
```bash
exp-cli list
```

Update an existing expense:
```bash
exp-cli update --id 1 --desc "Grocery shopping" --amt 160.00
```

Delete an expense:
```bash
exp-cli delete --id 1
```

Summarize expenses for November 2023:
```bash
exp-cli summary -m 11 -y 2023
```
