# Scenario-Based Question 2

## ATM Cash Withdrawal System

A bank wants to develop a simple ATM cash withdrawal system.

**Rules:**

* The user enters their account balance and the amount they want to withdraw.
* If the withdrawal amount is greater than the account balance, display **"Insufficient Balance"**.
* Otherwise, deduct the withdrawal amount from the account balance.
* Display the withdrawn amount and the remaining balance.

### Python Program

```python
# ATM Cash Withdrawal System

balance = float(input("Enter Account Balance: "))
withdraw = float(input("Enter Withdrawal Amount: "))

if withdraw > balance:
    print("Insufficient Balance")
else:
    balance = balance - withdraw
    print("\n------ ATM Receipt ------")
    print("Withdrawn Amount: ₹", withdraw)
    print("Remaining Balance: ₹", balance)
```

### Sample Output 1

```
Enter Account Balance: 5000
Enter Withdrawal Amount: 2000

------ ATM Receipt ------
Withdrawn Amount: ₹ 2000.0
Remaining Balance: ₹ 3000.0
```

### Sample Output 2

```
Enter Account Balance: 3000
Enter Withdrawal Amount: 5000

Insufficient Balance
```
