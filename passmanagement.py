Password Strength Checker

Question:
Write a Python program to check whether a password is strong. A strong password must:

Be at least 8 characters long.
Contain at least one digit.
Contain at least one uppercase letter.

Answer:

password = input("Enter Password: ")

has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
