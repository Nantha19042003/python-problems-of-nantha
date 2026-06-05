# Day 9 - Count the Number of Words in a Sentence

## Problem
Given a sentence, count how many words it contains.

---

## Example

Input:
```python
sentence = "Python is easy to learn"
```

Output:
```python
5
```

Explanation:
```python
The sentence contains 5 words.
```

---

## Python Code

```python
def count_words(sentence):
    words = sentence.split()
    return len(words)


sentence = "Python is easy to learn"

print(count_words(sentence))
```

---

## Simple Explanation

- Use `split()` to separate the sentence into words.
- Use `len()` to count the number of words.
- Return the total count.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 9: Counted the number of words in a sentence using Python
```
