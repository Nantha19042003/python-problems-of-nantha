# Day 7 - Find the Sum of All Numbers in a List

## Problem
Given a list of numbers, find the total sum of all elements.

---

## Example

Input:
```python
numbers = [10, 20, 30, 40]
```

Output:
```python
100
```

Explanation:
```python
10 + 20 + 30 + 40 = 100
```

---

## Python Code

```python
def find_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = [10, 20, 30, 40]

print(find_sum(numbers))
```

---

## Simple Explanation

- Start with a total value of 0.
- Go through each number in the list.
- Add each number to the total.
- Return the final total.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 7: Found the sum of all numbers in a list using Python
```
