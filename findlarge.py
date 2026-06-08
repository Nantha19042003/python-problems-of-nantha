# Day 12 - Find the Largest of Three Numbers

## Problem
Given three numbers, find the largest number among them.

---

## Example

Input:
```python
a = 15
b = 30
c = 20
```

Output:
```python
30
```

Explanation:
```python
30 is the largest among 15, 30, and 20.
```

---

## Python Code

```python
def find_largest(a, b, c):
    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    return largest


a = 15
b = 30
c = 20

print(find_largest(a, b, c))
```

---

## Simple Explanation

- Assume the first number is the largest.
- Compare it with the second number.
- Then compare it with the third number.
- Return the largest value.

---

## Time Complexity
```python
O(1)
```

---

## Commit Message
```bash
Day 12: Found the largest of three numbers using Python
```
