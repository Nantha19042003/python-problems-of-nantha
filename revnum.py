# Day 23 - Reverse a Number

## Problem
Given a number, reverse its digits.

---

## Example

Input:
```python
num = 1234
```

Output:
```python
4321
```

Explanation:
```python
The digits are reversed.
```

---

## Python Code

```python
def reverse_number(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return reversed_num


num = 1234

print(reverse_number(num))
```

---

## Simple Explanation

- Take the last digit using `% 10`.
- Add it to the reversed number.
- Remove the last digit using `// 10`.
- Repeat until the number becomes 0.
- Return the reversed number.

---

## Time Complexity
```python
O(n)
```

where `n` is the number of digits.

---

## Commit Message

```bash
Day 23: Reversed a number using Python
```
