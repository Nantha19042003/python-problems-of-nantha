# Day 18 - Find the Second Largest Number in a List

## Problem
Given a list of numbers, find the second largest number.

---

## Example

Input:
```python
numbers = [10, 25, 40, 15, 30]
```

Output:
```python
30
```

Explanation:
```python
40 is the largest number and 30 is the second largest.
```

---

## Python Code

```python
def second_largest(numbers):
    largest = max(numbers)
    numbers.remove(largest)

    return max(numbers)


numbers = [10, 25, 40, 15, 30]

print(second_largest(numbers))
```

---

## Simple Explanation

- Find the largest number in the list.
- Remove it from the list.
- Find the largest number again.
- The new largest number is the second largest.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 18: Found the second largest number in a list using Python
```
