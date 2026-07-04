1. Bank ATM System

Question:
A customer has ₹10,000 in their account. Write a Python program that allows them to deposit, withdraw, check their balance, and exit. Ensure they cannot withdraw more than their balance.

Ans:

balance = 10000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Available Balance:", balance)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
