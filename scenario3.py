# Scenario-Based Question 3

## Electricity Bill Calculator

An electricity board wants to calculate the electricity bill for its customers.

**Rules:**

* If the electricity consumption is **up to 100 units**, charge **₹2 per unit**.
* If the consumption is **101 to 200 units**, charge **₹3 per unit**.
* If the consumption is **above 200 units**, charge **₹5 per unit**.

**Task:**

1. Accept the number of units consumed from the user.
2. Calculate the electricity bill.
3. Display the units consumed and the total bill amount.

### Python Program

```python
# Electricity Bill Calculator

units = int(input("Enter Electricity Units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("\n------ Electricity Bill ------")
print("Units Consumed:", units)
print("Total Bill: ₹", bill)
```

### Sample Output 1

```
Enter Electricity Units: 80

------ Electricity Bill ------
Units Consumed: 80
Total Bill: ₹ 160
```

### Sample Output 2

```
Enter Electricity Units: 250

------ Electricity Bill ------
Units Consumed: 250
Total Bill: ₹ 1250
```
