# expense_tracker.py

import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        """Adds a new expense entry"""
        try:
            date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            if date_input:
                date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            else:
                date = datetime.date.today()

            category = input("Enter category (e.g., Food, Transport, Bills): ").strip()
            amount = self.get_valid_amount()
            description = input("Enter description: ").strip()

            self.expenses.append({
                'date': date,
                'category': category,
                'amount': amount,
                'description': description
            })
            print("✅ Expense added successfully.\n")
        except ValueError:
            print("❌ Invalid date format! Please use YYYY-MM-DD.\n")

    def get_valid_amount(self):
        while True:
            try:
                return float(input("Enter amount: "))
            except ValueError:
                print("❌ Please enter a valid number.")

    def view_expenses(self):
        """Displays all recorded expenses"""
        if not self.expenses:
            print("📭 No expenses recorded.\n")
            return
        print("\n📒 All Expenses:")
        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense['date']} | {expense['category']} | "
                  f"${expense['amount']:.2f} | {expense['description']}")
        print()

    def total_by_category(self):
        """Shows total expenses by specific category"""
        category = input("Enter category to calculate total: ").strip()
        total = sum(exp['amount'] for exp in self.expenses if exp['category'].lower() == category.lower())
        print(f"💰 Total spent in '{category}': ${total:.2f}\n")

    def total_expenses(self):
        """Shows total expenses overall"""
        total = sum(exp['amount'] for exp in self.expenses)
        print(f"💸 Total of all expenses: ${total:.2f}\n")

    def delete_expense(self):
        """Deletes an expense by entry number"""
        self.view_expenses()
        if not self.expenses:
            return
        try:
            entry = int(input("Enter the entry number to delete: "))
            if 1 <= entry <= len(self.expenses):
                deleted = self.expenses.pop(entry - 1)
                print(f"🗑️ Deleted: {deleted}\n")
            else:
                print("❌ Invalid entry number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

    def run(self):
        """Main loop"""
        while True:
            print("=== 🧾 Expense Tracker Menu ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Total by Category")
            print("4. Total of All Expenses")
            print("5. Delete Expense")
            print("6. Exit")

            choice = input("Select an option (1-6): ").strip()
            print()

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.total_by_category()
            elif choice == '4':
                self.total_expenses()
            elif choice == '5':
                self.delete_expense()
            elif choice == '6':
                print("👋 Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("❌ Invalid option, please try again.\n")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
