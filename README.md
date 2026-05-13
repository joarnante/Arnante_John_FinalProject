# Personal Finance Tracker 

# Description

The Personal Finance Tracker is a Command Line Interface (CLI) application developed in Python that helps users manage their daily finances. It allows users to record earnings and expenses, monitor their balance in real-time, and view a financial summary.

This project demonstrates key Python programming concepts such as object-oriented programming (classes and objects), file handling using JSON, data structures, input validation, and algorithmic logic.

---

# Objectives

- Apply Python programming concepts in a real-world scenario
- Build a functional CLI-based financial management system
- Demonstrate problem-solving using data processing and validation

---

# Features

- Add earnings and expense transactions
- Automatic detection of transaction type based on category
- View all transactions with + (earnings) and − (expense) indicators
- Color-coded interface using Colorama (green = earnings, red = expense)
- Real-time balance updates after every transaction
- Warning system when balance becomes negative (debt alert)
- Delete single or multiple transactions
- Confirmation prompt before deleting transactions
- Continuous input validation to prevent crashes
- Cancel/back option during category selection
- Currency formatting with peso sign and commas (₱10,000.00)
- Monthly summary report (total earnings, total expense, net balance)
- Exit message with a financial quote

---

# Technologies Used

- Python 3
- Colorama (for terminal text colors)
- JSON (for storing transaction data)

---

# Project Structure

```
<LastName_FirstName>_FinalProject/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── main.py        # Main CLI program
│   ├── manager.py     # Core logic (transactions, balance, delete, report)
│   ├── utils.py       # Input handling and validation
│   └── models.py      # Transaction class
│
└── data/
    └── transactions.json   # Stored financial data
```

---

# How to Run the Project

 - Install required library

# Run the application

```
 - python src/main.py
```

---

# Adding a Transaction

```
--- Personal Finance Tracker ---
1. Add Transaction

Choose Category:
1. Salary
2. Food
3. Bills
0. Back

Current Balance: 10,000.00
Enter amount for FOOD: 500
```

# Output

```
Transaction added as expense.
Updated Balance: ₱9,500.00
```

---

# Deleting Transactions

```
--- Transactions ---
1. earnings | Salary | ₱10,000.00
2. expense | Food | ₱500.00

Enter transaction numbers to delete: 2

Are you sure you want to delete these transaction(s)? (yes/no): yes
Transaction(s) deleted successfully.
```

---

# Monthly Report

```
--- Monthly Report ---
Total Earnings:  ₱10,000.00
Total Expense: ₱500.00
Net Balance:   ₱9,500.00
```

---

# Key Concepts Demonstrated

- Object-Oriented Programming (OOP)
- File Handling (JSON read/write)
- Data Structures (lists, dictionaries)
- Input Validation and Error Handling
- Looping and Conditional Logic
- Algorithmic thinking (safe deletion using reverse indexing)

---

# Video Demonstration

YouTube Link: https://youtu.be/k7v32P4dm-U?si=P22uQS25FspuruQp

---

# Author

Name: Arnante, John L.
Course: BSCS - 1B | INTERMEDIATE PROGRAMMING 

---

# Notes

- All transaction data is stored locally in a JSON file
- The application runs entirely in the terminal (CLI-based)
- Make sure Python is installed before running the program

---

# Future Improvements

- Add date tracking for transactions
- Filter transactions by month
- Export data to CSV
- Add graphical reports

---

# Screenshots

![Salary](image.png)
![View Transac](image-1.png)
![Monthly Summary - Exit](image-2.png)
