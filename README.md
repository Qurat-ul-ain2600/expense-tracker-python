# expense-tracker-python
# Expense Tracker Application

A simple **menu-driven Expense Tracker Application built in Python**. The application allows users to record, view, and analyze their daily expenses. All expense records are stored permanently in a CSV file.

## 📌 Project Overview

The Expense Tracker helps users maintain a record of their expenses by storing information such as:

* Date
* Category
* Amount
* Note

Users can add new expenses, view all recorded expenses along with the total amount spent, and generate a category-wise spending summary.

This project demonstrates fundamental Python programming concepts such as **functions, file handling, CSV files, loops, conditional statements, dictionaries, and exception handling**.

## ✨ Features

* Add new expense records
* Store expenses in a CSV file
* View all recorded expenses
* Calculate the total amount spent
* Display category-wise spending summaries
* Optional notes for individual expenses
* Validate expense amounts
* Handle invalid user input gracefully
* Handle missing or inaccessible files using exception handling
* Automatically create the CSV file if it does not exist

## 🛠️ Technologies Used

* **Python 3**
* **CSV Module**
* **OS Module**
* File Handling
* Exception Handling

## 📂 Project Structure

```text
expense-tracker-python/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

> `expenses.csv` is created automatically when the program is run if it does not already exist.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker-python.git
```

### 2. Open the project folder

```bash
cd expense-tracker-python
```

### 3. Run the Python program

```bash
python expense_tracker.py
```

## 📋 Main Menu

When the program runs, the following menu is displayed:

```text
====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. Category-wise Summary
4. Exit
```

### 1. Add Expense

The user can enter:

```text
Date: 2026-09-05
Category: Food
Amount: 250
Note: Lunch
```

The information is then saved to `expenses.csv`.

### 2. View Expenses

Displays all saved expenses and calculates the total amount spent.

Example:

```text
Date         Category        Amount     Note
-------------------------------------------------------
2026-09-05   Food            250.0      Lunch
2026-09-05   Transport       100.0      Bus fare
-------------------------------------------------------
Total Expense: 350.00
```

### 3. Category-wise Summary

The application calculates the total spending for each category.

Example:

```text
Category-wise Spending Summary
-----------------------------------
Food                 500.00
Transport            250.00
Shopping             800.00
```

### 4. Exit

Closes the application safely.

## 🧠 Python Concepts Demonstrated

This project demonstrates several important Python concepts:

### Functions

Separate functions are used for different tasks:

* `initialize_file()`
* `add_expense()`
* `view_expenses()`
* `category_summary()`
* `menu()`

### File Handling

The program uses Python's file-handling capabilities to read from and write to the CSV file.

### CSV Handling

The built-in `csv` module is used to store structured expense data.

### Exception Handling

`try-except` blocks are used to handle errors such as:

* Invalid amount input
* Missing CSV file
* Other unexpected errors

### Dictionaries

A dictionary is used to calculate category-wise spending totals.

## 🎯 Learning Objectives

By completing this project, the following concepts are practiced:

* Python functions
* Lists and dictionaries
* Loops and conditional statements
* User input
* File handling
* CSV data storage
* Exception handling
* Basic data processing
* Menu-driven programming

## 🚀 Future Improvements

Possible improvements include:

* Delete an expense
* Edit an existing expense
* Search expenses by date or category
* Filter expenses by month
* Set monthly spending limits
* Generate charts for spending patterns
* Export spending reports
* Add a graphical user interface (GUI)
* Use SQLite instead of CSV for larger datasets

## 👩‍💻 Author

**Qurat-ul-ain**

Data Science Student

## 📄 License

This project is created for **educational and learning purposes**.

