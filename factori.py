# Day 10 - Find the Factorial of a Number

## Problem
Given a positive integer, find its factorial.

The factorial of a number is the product of all positive integers from 1 to that number.

---

## Example

Input:
```python
num = 5
```

Output:
```python
120
```

Explanation:
```python
5! = 5 × 4 × 3 × 2 × 1 = 120
```

---

## Python Code

```python
def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result


num = 5

print(factorial(num))
```

---

## Simple Explanation

- Start with `result = 1`.
- Multiply it by each number from 1 to the given number.
- Return the final result.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 10: Calculated the factorial of a number using Python
```
