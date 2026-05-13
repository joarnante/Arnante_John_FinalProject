"""
Utility functions for the Personal Finance Tracker.

Handles user input validation and category selection
for transactions (earnings and expenses).
"""
from colorama import Fore
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
         print(Fore.RED + "Invalid number. Try again." + Fore.RESET)

def get_category_and_type():
    earnings_categories = ["Salary", "Freelance", "Received Allowance", "Gift", "Investment"]
    expense_categories = ["Food", "Bills", "Rent", "Transport", "Shopping", "Health"]

    print(Fore.BLUE + "\n--- Choose a Category ---" + Fore.RESET)

    all_categories = earnings_categories + expense_categories

    for i, cat in enumerate(all_categories, 1):
        print(f"{i}. {cat}")

    print("0. Back")

    while True:
        try:
            choice = int(input("Enter category number: "))

            if choice == 0:
                return None, None

            if 1 <= choice <= len(all_categories):
                category = all_categories[choice - 1]

                if category in earnings_categories:
                    t_type = "earnings"
                else:
                    t_type = "expense"

                return category, t_type

            else:
                print(Fore.RED + "Invalid choice." + Fore.RESET)

        except ValueError:
            print(Fore.RED + "Please enter a number." + Fore.RESET)