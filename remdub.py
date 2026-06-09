# Day 17 - Remove Duplicates from a List

## Problem
Given a list of numbers, remove duplicate values and return a new list containing only unique numbers.

---

## Example

Input:
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

Output:
```python
[1, 2, 3, 4, 5]
```

Explanation:
```python
Duplicate values 2 and 4 are removed.
```

---

## Python Code

```python
def remove_duplicates(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    return unique_numbers


numbers = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates(numbers))
```

---

## Simple Explanation

- Create an empty list.
- Go through each number in the original list.
- If the number is not already in the new list, add it.
- Return the list with unique values.

---

## Time Complexity
```python
O(n²)
```

---

## Commit Message

```bash
Day 17: Removed duplicate values from a list using Python
```
