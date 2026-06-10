# Day 21 - Count Even and Odd Numbers in a List

## Problem
Given a list of numbers, count how many even numbers and odd numbers are present.

---

## Example

Input:
```python
numbers = [1, 2, 3, 4, 5, 6]
```

Output:
```python
Even Numbers: 3
Odd Numbers: 3
```

Explanation:
```python
Even numbers are 2, 4, 6
Odd numbers are 1, 3, 5
```

---

## Python Code

```python
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even Numbers:", even_count)
    print("Odd Numbers:", odd_count)


numbers = [1, 2, 3, 4, 5, 6]

count_even_odd(numbers)
```

---

## Simple Explanation

- Go through each number in the list.
- If the number is divisible by 2, count it as even.
- Otherwise, count it as odd.
- Display the total counts.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 21: Counted even and odd numbers in a list using Python
```
