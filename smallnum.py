# Day 8 - Find the Smallest Number in a List

## Problem
Given a list of numbers, find the smallest number.

---

## Example

Input:
```python
numbers = [10, 25, 5, 40, 15]
```

Output:
```python
5
```

Explanation:
```python
5 is the smallest number in the list.
```

---

## Python Code

```python
def find_smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


numbers = [10, 25, 5, 40, 15]

print(find_smallest(numbers))
```

---

## Simple Explanation

- Assume the first number is the smallest.
- Check each number in the list.
- If a smaller number is found, update the smallest value.
- Return the smallest number.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 8: Found the smallest number in a list using Python
```
