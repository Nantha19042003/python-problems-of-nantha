# Day 14 - Find the Length of a String

## Problem
Given a string, find the total number of characters in it.

---

## Example

Input:
```python
text = "Python"
```

Output:
```python
6
```

Explanation:
```python
The word "Python" contains 6 characters.
```

---

## Python Code

```python
def string_length(text):
    count = 0

    for char in text:
        count += 1

    return count


text = "Python"

print(string_length(text))
```

---

## Simple Explanation

- Start a counter with 0.
- Go through each character in the string.
- Increase the counter by 1 for every character.
- Return the final count.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 14: Found the length of a string using Python
```
