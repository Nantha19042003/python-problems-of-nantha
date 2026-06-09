# Day 16 - Count the Occurrences of a Character in a String

## Problem
Given a string and a character, count how many times the character appears in the string.

---

## Example

Input:
```python
text = "programming"
char = "m"
```

Output:
```python
2
```

Explanation:
```python
The character "m" appears 2 times in "programming".
```

---

## Python Code

```python
def count_character(text, char):
    count = 0

    for letter in text:
        if letter == char:
            count += 1

    return count


text = "programming"
char = "m"

print(count_character(text, char))
```

---

## Simple Explanation

- Start a counter with 0.
- Check each character in the string.
- If it matches the given character, increase the counter.
- Return the final count.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message

```bash
Day 16: Counted character occurrences in a string using Python
```
