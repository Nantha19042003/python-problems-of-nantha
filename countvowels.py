# Day 5 - Count Vowels in a String

## Problem
Given a string, count how many vowels (`a, e, i, o, u`) are present in it.

---

## Example

Input:
```python
text = "Hello World"
```

Output:
```python
3
```

Explanation:
```python
The vowels are: e, o, o
```

---

## Python Code

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


text = "Hello World"

print(count_vowels(text))
```

---

## Simple Explanation

- Create a list of vowels.
- Check each character in the string.
- If the character is a vowel, increase the count.
- Return the total count.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 5: Counted vowels in a string using Python
```
