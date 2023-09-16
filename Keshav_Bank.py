import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            messagebox.showwarning("Insufficient Funds", "Not enough balance to withdraw.")

    def get_balance(self):
        return self.balance

def create_account():
    account_number = account_number_entry.get()
    account_holder = account_holder_entry.get()
    initial_balance = initial_balance_entry.get()
    
    if not account_number or not account_holder or not initial_balance:
        messagebox.showwarning("Missing Information", "Please fill in all fields.")
        return

    try:
        initial_balance = float(initial_balance)
        if initial_balance < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid initial balance.")
        return

    account = BankAccount(account_number, account_holder, initial_balance)
    accounts.append(account)
    messagebox.showinfo("Account Created", f"Account {account_number} for {account_holder} created with an initial balance of ${initial_balance}.")
    clear_entries()

def deposit():
    account_number = account_number_entry.get()
    amount = deposit_amount_entry.get()

    if not account_number or not amount:
        messagebox.showwarning("Missing Information", "Please fill in both fields.")
        return

    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid amount to deposit.")
        return

    account = find_account(account_number)
    if account:
        account.deposit(amount)
        messagebox.showinfo("Deposit Successful", f"${amount} deposited into Account {account_number}. New balance: ${account.get_balance()}.")
    else:
        messagebox.showwarning("Account Not Found", f"Account {account_number} not found.")
    clear_entries()

def withdraw():
    account_number = account_number_entry.get()
    amount = withdraw_amount_entry.get()

    if not account_number or not amount:
        messagebox.showwarning("Missing Information", "Please fill in both fields.")
        return

    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid amount to withdraw.")
        return

    account = find_account(account_number)
    if account:
        account.withdraw(amount)
        messagebox.showinfo("Withdrawal Successful", f"${amount} withdrawn from Account {account_number}. New balance: ${account.get_balance()}.")
    else:
        messagebox.showwarning("Account Not Found", f"Account {account_number} not found.")
    clear_entries()

def check_balance():
    account_number = account_number_entry.get()

    if not account_number:
        messagebox.showwarning("Missing Information", "Please enter an account number.")
        return

    account = find_account(account_number)
    if account:
        messagebox.showinfo("Balance Inquiry", f"Account {account_number} balance: ${account.get_balance()}.")
    else:
        messagebox.showwarning("Account Not Found", f"Account {account_number} not found.")
    clear_entries()

def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

def clear_entries():
    account_number_entry.delete(0, tk.END)
    account_holder_entry.delete(0, tk.END)
    initial_balance_entry.delete(0, tk.END)
    deposit_amount_entry.delete(0, tk.END)
    withdraw_amount_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Bank Application")

# Create and initialize a list to store accounts
accounts = []

# Create and configure GUI components
account_number_label = tk.Label(root, text="Account Number:")
account_holder_label = tk.Label(root, text="Account Holder:")
initial_balance_label = tk.Label(root, text="Initial Balance:")
deposit_amount_label = tk.Label(root, text="Deposit Amount:")
withdraw_amount_label = tk.Label(root, text="Withdraw Amount:")

account_number_entry = tk.Entry(root)
account_holder_entry = tk.Entry(root)
initial_balance_entry = tk.Entry(root)
deposit_amount_entry = tk.Entry(root)
withdraw_amount_entry = tk.Entry(root)

create_button = tk.Button(root, text="Create Account", command=create_account)
deposit_button = tk.Button(root, text="Deposit", command=deposit)
withdraw_button = tk.Button(root, text="Withdraw", command=withdraw)
balance_button = tk.Button(root, text="Check Balance", command=check_balance)

# Arrange GUI components using grid layout
account_number_label.grid(row=0, column=0)
account_holder_label.grid(row=1, column=0)
initial_balance_label.grid(row=2, column=0)
deposit_amount_label.grid(row=3, column=0)
withdraw_amount_label.grid(row=4, column=0)

account_number_entry.grid(row=0, column=1)
account_holder_entry.grid(row=1, column=1)
initial_balance_entry.grid(row=2, column=1)
deposit_amount_entry.grid(row=3, column=1)
withdraw_amount_entry.grid(row=4, column=1)

create_button.grid(row=5, column=0, columnspan=2)
deposit_button.grid(row=6, column=0, columnspan=2)
withdraw_button.grid(row=7, column=0, columnspan=2)
balance_button.grid(row=8, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
#keshav singh interPE
