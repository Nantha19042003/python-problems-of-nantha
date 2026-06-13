# Day 27 - Find the GCD (Greatest Common Divisor)

## Problem
Given two numbers, find their Greatest Common Divisor (GCD).

The GCD is the largest number that divides both numbers without leaving a remainder.

---

## Example

Input:
```python
a = 12
b = 18
```

Output:
```python
6
```

Explanation:
```python
Factors of 12: 1, 2, 3, 4, 6, 12
Factors of 18: 1, 2, 3, 6, 9, 18

Greatest Common Divisor = 6
```

---

## Python Code

```python
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print(find_gcd(12, 18))
```

---

## Simple Explanation

- Divide the larger number by the smaller number.
- Find the remainder.
- Replace the numbers and repeat.
- When remainder becomes 0, the GCD is found.

---

## Time Complexity
```python
O(log n)
```

---

## Commit Message

```bash
Day 27: Found the GCD of two numbers using Python
```
