"""
Finance Manager Module

Handles all core financial operations including adding, storing,
loading, and managing transactions. It also calculates balance,
provides summaries, and persists data using a JSON file.
"""
import json
from models import Transaction

from colorama import Fore
class FinanceManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []
        self.load_data()

    def add_transaction(self, amount, category, t_type):

        if t_type == "expense":
            current_balance = self.get_balance()

            if amount > current_balance:
                print(Fore.RED + f"\n⚠ Warning: This expense exceeds your current balance (₱{current_balance:,.2f})" + Fore.RESET)

                confirm = input("Do you want to continue? (yes/no): ").lower()

                if confirm != "yes":
                    print(Fore.GREEN + "Transaction cancelled." + Fore.RESET)
                    return

        transaction = Transaction(amount, category, t_type)
        self.transactions.append(transaction)
        self.save_data()

    def get_balance(self):
        earnings = sum(t.amount for t in self.transactions if t.type == "earnings")
        expense = sum(t.amount for t in self.transactions if t.type == "expense")
        return earnings - expense

    def list_transactions(self):
        return self.transactions

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump([t.to_dict() for t in self.transactions], file, indent=4)

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.transactions = [
                    Transaction(d["amount"], d["category"], d["type"]) for d in data
                ]
        except FileNotFoundError:
            self.transactions = []

    def delete_transaction(self, index):
         if 0 <= index < len(self.transactions):
             del self.transactions[index]
             self.save_data()
             return True
         return False
    
    def get_summary(self):
         earnings = sum(t.amount for t in self.transactions if t.type == "earnings")
         expense = sum(t.amount for t in self.transactions if t.type == "expense")
         return earnings, expense, earnings - expense