# Day 19 - Check if Two Strings are Anagrams

## Problem
Given two strings, check whether they are anagrams.

Two strings are anagrams if they contain the same characters in a different order.

---

## Example 1

Input:
```python
str1 = "listen"
str2 = "silent"
```

Output:
```python
Anagram
```

---

## Example 2

Input:
```python
str1 = "hello"
str2 = "world"
```

Output:
```python
Not an Anagram
```

---

## Python Code

```python
def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return "Anagram"
    else:
        return "Not an Anagram"


str1 = "listen"
str2 = "silent"

print(check_anagram(str1, str2))
```

---

## Simple Explanation

- Sort the characters of both strings.
- Compare the sorted strings.
- If they are the same, the strings are anagrams.
- Otherwise, they are not anagrams.

---

## Time Complexity
```python
O(n log n)
```

---

## Commit Message

```bash
Day 19: Checked whether two strings are anagrams using Python
```
