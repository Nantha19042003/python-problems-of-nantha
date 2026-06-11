# Day 22 - Find the Sum of Digits of a Number

## Problem
Given a number, find the sum of all its digits.

---

## Example

Input:
```python
num = 1234
```

Output:
```python
10
```

Explanation:
```python
1 + 2 + 3 + 4 = 10
```

---

## Python Code

```python
def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    return total


num = 1234

print(sum_of_digits(num))
```

---

## Simple Explanation

- Take the last digit using `% 10`.
- Add it to the total.
- Remove the last digit using `// 10`.
- Repeat until the number becomes 0.
- Return the total sum.

---

## Time Complexity
```python
O(n)
```

where `n` is the number of digits.

---

## Commit Message

```bash
Day 22: Calculated the sum of digits of a number using Python
```
