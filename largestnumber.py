# Day 3 - Find the Largest Number in a List

## Problem
Given a list of numbers, find and return the largest number.

---

## Example

Input:
```python
numbers = [10, 25, 5, 40, 15]
```

Output:
```python
40
```

Explanation:
```python
40 is the largest number in the list.
```

---

## Python Code

```python
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [10, 25, 5, 40, 15]

print(find_largest(numbers))
```

---

## Simple Explanation

- Assume the first number is the largest.
- Check every number in the list.
- If a bigger number is found, update the largest value.
- Return the largest number at the end.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 3: Found the largest number in a list using Python
```
