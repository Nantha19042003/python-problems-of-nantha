# Day 35 - Find the Sum of Numbers Using Recursion

## Problem
Given a number n, find the sum of numbers from 1 to n using recursion.

---

## Example

Input:
```python
n = 5
```

Output:
```python
15
```

Explanation:
```python
1 + 2 + 3 + 4 + 5 = 15
```

---

## Python Code

```python
def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)


print(sum_numbers(5))
```

---

## Simple Explanation

- If n is 1, return 1.
- Otherwise add n to the sum of numbers before it.
- The function keeps calling itself until it reaches 1.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 35: Calculated sum of numbers using recursion in Python
```
