# Day 28 - Find the LCM (Least Common Multiple)

## Problem
Given two numbers, find their Least Common Multiple (LCM).

The LCM is the smallest number that is divisible by both numbers.

---

## Example

Input:
```python
a = 12
b = 18
```

Output:
```python
36
```

Explanation:
```python
36 is the smallest number divisible by both 12 and 18.
```

---

## Python Code

```python
def find_lcm(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


print(find_lcm(12, 18))
```

---

## Simple Explanation

- Start from the larger number.
- Check if it is divisible by both numbers.
- If not, increase by 1 and check again.
- The first matching number is the LCM.

---

## Time Complexity
```python
O(a × b)
```

---

## Commit Message

```bash
Day 28: Found the LCM of two numbers using Python
```
