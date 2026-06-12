# Day 24 - Check if a Number is Armstrong Number

## Problem
Given a number, check whether it is an Armstrong number.

An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.

---

## Example

Input:
```python
num = 153
```

Output:
```python
Armstrong Number
```

Explanation:
```python
1³ + 5³ + 3³ = 1 + 125 + 27 = 153
```

So, 153 is an Armstrong number.

---

## Python Code

```python
def is_armstrong(num):
    digits = str(num)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == num:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"


num = 153

print(is_armstrong(num))
```

---

## Simple Explanation

- Count the number of digits.
- Raise each digit to that power.
- Add all the values together.
- If the total equals the original number, it is an Armstrong number.

---

## Time Complexity
```python
O(n)
```

where `n` is the number of digits.

---

## Commit Message

```bash
Day 24: Checked whether a number is an Armstrong number using Python
```
