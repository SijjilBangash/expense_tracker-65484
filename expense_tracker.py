# expense_tracker.py

import datetime

# Global list to store all expenses
expenses = []

def add_expense():
    """Adds a new expense entry"""
    try:
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if date_input:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        else:
            date = datetime.date.today()

        category = input("Enter category (e.g., Food, Transport, Bills): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expenses.append({
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        })
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid input! Please try again.\n")

def view_expenses():
    """Displays all recorded expenses"""
    if not expenses:
        print("No expenses recorded.\n")
        return
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
              f"Amount: {expense['amount']}, Description: {expense['description']}")
    print()

def total_by_category():
    """Shows total expenses by specific category"""
    category = input("Enter category to calculate total: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total spent in '{category}': {total}\n")

def delete_expense():
    """Deletes an expense by entry number"""
    view_expenses()
    try:
        entry = int(input("Enter the entry number to delete: "))
        if 1 <= entry <= len(expenses):
            deleted = expenses.pop(entry - 1)
            print(f"Deleted: {deleted}\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    """Main loop for the expense tracker"""
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total by Category")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Select an option (1-5): ")
        print()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()
