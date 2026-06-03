# Day 6 - Check Even or Odd Number

## Problem
Given a number, check whether it is even or odd.

---

## Example 1

Input:
```python
num = 8
```

Output:
```python
Even
```

---

## Example 2

Input:
```python
num = 7
```

Output:
```python
Odd
```

---

## Python Code

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = 8

print(check_even_odd(num))
```

---

## Simple Explanation

- Divide the number by 2.
- If the remainder is 0, the number is Even.
- Otherwise, the number is Odd.

---

## Time Complexity
```python
O(1)
```

---

## Commit Message
```bash
Day 6: Checked whether a number is even or odd using Python
```
