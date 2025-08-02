# bank-account
This is a simple Object-Oriented Programming (OOP) project in Python that simulates a basic banking system. It includes features like account creation, deposits, withdrawals, transfers, interest rewards, and balance checking — along with error handling using custom exceptions.

🚀 Features
Create bank accounts with initial balance and account name

Deposit and withdraw money with balance validation

Transfer funds between accounts

Interest-based accounts with bonus on deposits

Savings accounts with withdrawal fees

Custom balanceException for insufficient funds

🧱 Classes Overview
bankAccount: Base class with core functionality

interestrewardsacct: Inherits from bankAccount, adds 5% interest on each deposit

savingacct: Inherits from interestrewardsacct, adds withdrawal fee

balanceException: Custom exception raised when insufficient balance exists

📂 Files
bank_accounts.py: Core logic for account classes and exception handling

main.py (optional): Example of how to use the classes interactively


