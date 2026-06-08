# Day 13 - Check if a String is a Palindrome

## Problem
Given a string, check whether it reads the same forward and backward.

A palindrome word remains the same when reversed.

---

## Example 1

Input:
```python
text = "madam"
```

Output:
```python
Palindrome
```

---

## Example 2

Input:
```python
text = "python"
```

Output:
```python
Not a Palindrome
```

Explanation:
```python
"python" reversed is "nohtyp"
```

---

## Python Code

```python
def is_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"


text = "madam"

print(is_palindrome(text))
```

---

## Simple Explanation

- Reverse the string using `[::-1]`.
- Compare the reversed string with the original string.
- If both are the same, it is a palindrome.
- Otherwise, it is not a palindrome.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 13: Checked whether a string is a palindrome using Python
```
