# Day 2 - Palindrome Number

## Problem
Given an integer `x`, return `True` if the number is a palindrome, otherwise return `False`.

A palindrome number reads the same forward and backward.

---

## Example 1

Input:
```python
x = 121
```

Output:
```python
True
```

Explanation:
```python
121 reversed is also 121
```

---

## Example 2

Input:
```python
x = 123
```

Output:
```python
False
```

Explanation:
```python
123 reversed is 321
```

---

## Python Code

```python
def is_palindrome(x):
    original = str(x)
    reversed_num = original[::-1]

    return original == reversed_num


x = 121

print(is_palindrome(x))
```

---

## Simple Explanation

- Convert the number into a string.
- Reverse the string using slicing.
- Compare original and reversed values.
- If both are same, it is a palindrome.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 2: Solved Palindrome Number problem in Python
```
