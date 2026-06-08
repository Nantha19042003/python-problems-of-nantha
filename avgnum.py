# Day 15 - Find the Average of Numbers in a List

## Problem
Given a list of numbers, find the average (mean) of all the numbers.

---

## Example

Input:
```python
numbers = [10, 20, 30, 40, 50]
```

Output:
```python
30.0
```

Explanation:
```python
(10 + 20 + 30 + 40 + 50) / 5 = 30.0
```

---

## Python Code

```python
def find_average(numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return average


numbers = [10, 20, 30, 40, 50]

print(find_average(numbers))
```

---

## Simple Explanation

- Add all the numbers in the list.
- Count how many numbers are in the list.
- Divide the total by the count.
- Return the average value.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 15: Calculated the average of numbers in a list using Python
```
