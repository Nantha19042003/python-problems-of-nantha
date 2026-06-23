# Day 34 - Print a Right Triangle Star Pattern

## Problem
Print a right triangle pattern using stars.

---

## Example

Output:
```python
*
**
***
****
*****
```

---

## Python Code

```python
rows = 5

for i in range(1, rows + 1):
    print("*" * i)
```

---

## Simple Explanation

- Start from 1 star.
- Increase the number of stars in each row.
- Continue until the required number of rows is printed.

---

## Time Complexity
```python
O(n²)
```

---

## Commit Message

```bash
Day 34: Printed a right triangle star pattern using Python
```
