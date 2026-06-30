**Library Fine Calculator**

A college library issues books to students. If a student returns a book after the due date, a fine is charged based on the following rules:

* If the book is returned on or before the due date (0 or fewer late days), the fine is **₹0**.
* If the book is returned **1 to 5 days late**, the fine is **₹10 per day**.
* If the book is returned **6 to 10 days late**, the fine is **₹20 per day**.
* If the book is returned **more than 10 days late**, the fine is **₹50 per day**.

**Task:**

1. Accept the number of late days from the user.
2. Calculate the fine according to the rules.
3. Display the number of late days and the total fine.

**Python Program:**

```python
# Library Fine Calculator

late_days = int(input("Enter the number of late days: "))

if late_days <= 0:
    fine = 0
elif late_days <= 5:
    fine = late_days * 10
elif late_days <= 10:
    fine = late_days * 20
else:
    fine = late_days * 50

print("\n------ Library Fine Details ------")
print("Late Days :", late_days)
print("Total Fine: ₹", fine)
```

**Sample Output 1:**

```
Enter the number of late days: 4

------ Library Fine Details ------
Late Days : 4
Total Fine: ₹ 40
```

**Sample Output 2:**

```
Enter the number of late days: 12

------ Library Fine Details ------
Late Days : 12
Total Fine: ₹ 600
```
