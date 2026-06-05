# Day 11 - Check if a Number is Prime

## Problem
Given a positive integer, check whether it is a prime number.

A prime number is a number greater than 1 that is divisible only by 1 and itself.

---

## Example 1

Input:
```python
num = 7
```

Output:
```python
Prime Number
```

---

## Example 2

Input:
```python
num = 8
```

Output:
```python
Not a Prime Number
```

Explanation:
```python
8 is divisible by 2 and 4, so it is not a prime number.
```

---

## Python Code

```python
def is_prime(num):
    if num <= 1:
        return "Not a Prime Number"

    for i in range(2, num):
        if num % i == 0:
            return "Not a Prime Number"

    return "Prime Number"


num = 7

print(is_prime(num))
```

---

## Simple Explanation

- Prime numbers are greater than 1.
- Check if the number can be divided by any number between 2 and itself.
- If divisible, it is not prime.
- Otherwise, it is a prime number.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 11: Checked whether a number is prime using Python
```
