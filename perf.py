# Day 26 - Check if a Number is Perfect Number

## Problem
Given a number, check whether it is a Perfect Number.

A Perfect Number is a number that is equal to the sum of its proper divisors (excluding itself).

---

## Example

Input:
```python
num = 6
```

Output:
```python
Perfect Number
```

Explanation:
```python
Divisors of 6 are 1, 2, 3

1 + 2 + 3 = 6
```

So, 6 is a Perfect Number.

---

## Python Code

```python
def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"


num = 6

print(is_perfect(num))
```

---

## Simple Explanation

- Find all divisors of the number except itself.
- Add all the divisors.
- If the sum equals the original number, it is a Perfect Number.
- Otherwise, it is not.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 26: Checked whether a number is a Perfect Number using Python
```
