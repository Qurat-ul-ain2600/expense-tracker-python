import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file with headers if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


# Add a new expense
def add_expense():
    try:
        date = input("Enter Date (YYYY-MM-DD): ").strip()
        category = input("Enter Category: ").strip()

        amount = float(input("Enter Amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        note = input("Enter Note (optional): ").strip()

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.")
    except Exception as e:
        print("Error:", e)


# View all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("\nNo expense records found.")
                return

            print("\n{:<12} {:<15} {:<10} {}".format(
                "Date", "Category", "Amount", "Note"))
            print("-" * 55)

            total = 0

            for row in rows[1:]:
                print("{:<12} {:<15} {:<10} {}".format(
                    row[0], row[1], row[2], row[3]))
                total += float(row[2])

            print("-" * 55)
            print("Total Expense: {:.2f}".format(total))

    except FileNotFoundError:
        print("Expense file not found.")
    except Exception as e:
        print("Error:", e)


# Display category-wise summary
def category_summary():
    try:
        summary = {}

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                category = row["Category"]
                amount = float(row["Amount"])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        if not summary:
            print("\nNo expense records found.")
            return

        print("\nCategory-wise Spending Summary")
        print("-" * 35)

        for category, amount in summary.items():
            print("{:<20} {:.2f}".format(category, amount))

    except FileNotFoundError:
        print("Expense file not found.")
    except Exception as e:
        print("Error:", e)


# Main menu
def menu():
    initialize_file()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    menu()