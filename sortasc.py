# Day 29 - Sort a List in Ascending Order

## Problem
Given a list of numbers, sort them in ascending order.

Ascending order means smallest number to largest number.

---

## Example

Input:
```python
numbers = [5, 2, 8, 1, 9]
```

Output:
```python
[1, 2, 5, 8, 9]
```

Explanation:
```python
Numbers are arranged from smallest to largest.
```

---

## Python Code

```python
def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


numbers = [5, 2, 8, 1, 9]

print(sort_numbers(numbers))
```

---

## Simple Explanation

- Compare each number with the remaining numbers.
- Swap if a smaller number is found.
- Continue until the list is sorted.
- Return the sorted list.

---

## Time Complexity
```python
O(n²)
```

---

## Commit Message

```bash
Day 29: Sorted a list in ascending order using Python
```
