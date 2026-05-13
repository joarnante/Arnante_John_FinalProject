"""
Personal Finance Tracker - CLI Application

This module runs a command-line interface for managing personal
financial transactions. Users can add, view, delete transactions,
check balance, and generate monthly reports.

Data is stored in a JSON file and handled through FinanceManager.
"""
from manager import FinanceManager
from utils import get_float_input, get_category_and_type
from colorama import init, Fore

init()

def main():
    manager = FinanceManager("data/transactions.json")

    while True:
        print(Fore.BLUE + "\n--- Personal Finance Tracker ---" + Fore.RESET)
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Delete Transaction")
        print("5. Monthly Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
             category, t_type = get_category_and_type()

             if category is None:
                 print(Fore.LIGHTRED_EX + "Transaction cancelled." + Fore.RESET)
                 continue

             current_balance = manager.get_balance()
             current_color = Fore.RED if current_balance < 0 else Fore.GREEN

             print(f"\nCurrent Balance: " + current_color + f"₱{current_balance:,.2f}" + Fore.RESET)

             amount = get_float_input(
    f"Enter amount for {Fore.YELLOW}{category}{Fore.RESET}: "
)

             manager.add_transaction(amount, category, t_type)

             new_balance = manager.get_balance()
             print(Fore.LIGHTBLUE_EX + f"\nTransaction added as {t_type}." + Fore.RESET)
             updated_color = Fore.RED if new_balance < 0 else Fore.GREEN

             print("Updated Balance: " + updated_color + f"₱{new_balance:,.2f}" + Fore.RESET)

        elif choice == "2":
             transactions = manager.list_transactions()

             if not transactions:
                 print(Fore.RED + "No transactions yet." + Fore.RESET)
             else:
                 for t in transactions:
                     if t.type == "earnings":
                         sign = "+"
                         color = Fore.GREEN
                     else:
                         sign = "-"
                         color = Fore.RED

                     print(
                         color +
                         f"{sign} ₱{t.amount:,.2f} | {t.category} | {t.type.upper()}"
                         + Fore.RESET
                     )

        elif choice == "3":
             balance = manager.get_balance()

             if balance < 0:
                 color = Fore.RED
             else:
                 color = Fore.GREEN

             print(f"Balance: " + color + f"₱{balance:,.2f}" + Fore.RESET)
             if balance < 0:
              print(Fore.RED + "⚠ WARNING: You are in debt!" + Fore.RESET)

        elif choice == "4":
             transactions = manager.list_transactions()

             if not transactions:
                 print(Fore.RED + "No transactions to delete." + Fore.RESET)
                 continue

             print(Fore.BLUE + "\n--- Transactions ---" + Fore.RESET)
             for i, t in enumerate(transactions):
                 print(f"{i+1}. {t.type} | {t.category} | ₱{t.amount:,.2f}")

             while True:
                 user_input = input("Enter transaction numbers to delete (e.g. 1,3) or 0 to cancel: ")

                 if user_input == "0":
                     print(Fore.GREEN + "Deletion cancelled." + Fore.RESET)
                     break

                 try:
                     indexes = [int(x.strip()) - 1 for x in user_input.split(",")]

                     if any(i < 0 or i >= len(transactions) for i in indexes):
                         print(Fore.RED + "Invalid selection. Try again." + Fore.RESET)
                         continue

                     indexes = sorted(set(indexes), reverse=True)

                     print(Fore.YELLOW + "\nYou selected:" + Fore.RESET)
                     for i in indexes:
                         t = transactions[i]
                         print(f"{i+1}. {t.type} | {t.category} | ₱{t.amount:,.2f}")

                     confirm = input(Fore.RED + "\nAre you sure you want to delete these transaction(s)? (yes/no): " + Fore.RESET).lower()

                     if confirm != "yes":
                         print(Fore.GREEN + "Deletion cancelled." + Fore.RESET)
                         break

                     for i in indexes:
                         manager.delete_transaction(i)

                     print(Fore.GREEN + "Transaction(s) deleted successfully." + Fore.RESET)
                     break

                 except ValueError:
                     print(Fore.RED + "Please enter valid numbers separated by commas." + Fore.RESET)

        elif choice == "5":
             earnings, expense, net = manager.get_summary()

             print(Fore.BLUE + "\n--- Monthly Report ---" + Fore.RESET)
             print(f"Total Earnings:  ₱{earnings:,.2f}")
             print(f"Total Expense: ₱{expense:,.2f}")

             if net < 0:
                 color = Fore.RED
             else:
                 color = Fore.GREEN

             print(f"Net Balance:   " + color + f"₱{net:,.2f}" + Fore.RESET)

        elif choice == "6":
             print(Fore.LIGHTMAGENTA_EX + "\nFinance Tracker Closed!" + Fore.RESET)
             print(Fore.BLUE + "\"Every peso counts. Manage it well.\"" + Fore.RESET)
             break

        else:
            print(Fore.RED + "Invalid choice." + Fore.RESET)

if __name__ == "__main__":
    main()