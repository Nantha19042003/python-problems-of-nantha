# ==========================================================
# SCENARIO 11: MOVIE TICKET BOOKING SYSTEM
# ==========================================================

# Question:
# Calculate the total ticket amount.
# Ticket Price = ₹200 per person.
# If more than 5 tickets are booked, give a 10% discount.

print("===== MOVIE TICKET BOOKING =====")

name = input("Enter Customer Name: ")
tickets = int(input("Enter Number of Tickets: "))

price = tickets * 200

if tickets > 5:
    discount = price * 10 / 100
else:
    discount = 0

total = price - discount

print("Customer Name :", name)
print("Total Amount :", total)


# ==========================================================
# SCENARIO 12: MOBILE RECHARGE SYSTEM
# ==========================================================

# Question:
# Display recharge plans and calculate the total amount.

print("\n===== MOBILE RECHARGE SYSTEM =====")

print("1. ₹199")
print("2. ₹399")
print("3. ₹599")

choice = int(input("Select Plan: "))

if choice == 1:
    amount = 199
elif choice == 2:
    amount = 399
elif choice == 3:
    amount = 599
else:
    amount = 0

print("Recharge Amount :", amount)


# ==========================================================
# SCENARIO 13: HOTEL ROOM BOOKING SYSTEM
# ==========================================================

# Question:
# Calculate room rent.
# Deluxe = ₹3000
# Standard = ₹2000
# Economy = ₹1000

print("\n===== HOTEL ROOM BOOKING =====")

print("1. Deluxe")
print("2. Standard")
print("3. Economy")

room = int(input("Choose Room Type: "))
days = int(input("Number of Days: "))

if room == 1:
    rent = 3000 * days
elif room == 2:
    rent = 2000 * days
elif room == 3:
    rent = 1000 * days
else:
    rent = 0

print("Total Room Rent :", rent)


# ==========================================================
# SCENARIO 14: SIMPLE CALCULATOR
# ==========================================================

# Question:
# Perform Addition, Subtraction,
# Multiplication and Division.

print("\n===== SIMPLE CALCULATOR =====")

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Answer =", a + b)
elif choice == 2:
    print("Answer =", a - b)
elif choice == 3:
    print("Answer =", a * b)
elif choice == 4:
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Division by Zero Not Allowed")
else:
    print("Invalid Choice")


# ==========================================================
# SCENARIO 15: VOTER ELIGIBILITY SYSTEM
# ==========================================================

# Question:
# Check whether a person is eligible to vote.

print("\n===== VOTER ELIGIBILITY =====")

name = input("Enter Name: ")
age = int(input("Enter Age: "))

if age >= 18:
    print(name, "is Eligible to Vote")
else:
    print(name, "is Not Eligible to Vote")


# ==========================================================
# SCENARIO 16: PASSWORD VERIFICATION
# ==========================================================

# Question:
# Verify password.
# Password = python123

print("\n===== PASSWORD VERIFICATION =====")

password = input("Enter Password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")


# ==========================================================
# SCENARIO 17: BANK LOAN ELIGIBILITY
# ==========================================================

# Question:
# Customer is eligible if salary is ₹30000 or above.

print("\n===== BANK LOAN ELIGIBILITY =====")

salary = float(input("Enter Monthly Salary: "))

if salary >= 30000:
    print("Loan Approved")
else:
    print("Loan Rejected")


# ==========================================================
# SCENARIO 18: ODD OR EVEN NUMBER
# ==========================================================

# Question:
# Check whether a number is odd or even.

print("\n===== ODD OR EVEN =====")

num = int(input("Enter Number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ==========================================================
# SCENARIO 19: FACTORIAL OF A NUMBER
# ==========================================================

# Question:
# Find the factorial of a given number.

print("\n===== FACTORIAL =====")

num = int(input("Enter Number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


# ==========================================================
# SCENARIO 20: NUMBER GUESSING GAME
# ==========================================================

# Question:
# Guess the secret number.

print("\n===== NUMBER GUESSING GAME =====")

secret = 7

guess = int(input("Guess the Number (1-10): "))

if guess == secret:
    print("Congratulations! Correct Guess")
else:
    print("Wrong Guess")
    print("Correct Number is", secret)
