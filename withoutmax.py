# Day 20 - Find the Maximum Number in a List Without Using max()

## Problem
Given a list of numbers, find the largest number without using Python's built-in `max()` function.

---

## Example

Input:
```python
numbers = [12, 45, 7, 89, 23]
```

Output:
```python
89
```

Explanation:
```python
89 is the largest number in the list.
```

---

## Python Code

```python
def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [12, 45, 7, 89, 23]

print(find_max(numbers))
```

---

## Simple Explanation

- Assume the first number is the largest.
- Compare it with every other number in the list.
- If a larger number is found, update the largest value.
- Return the largest number at the end.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 20: Found the largest number in a list without using max()
```
