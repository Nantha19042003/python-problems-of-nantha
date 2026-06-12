# Day 25 - Generate Fibonacci Series

## Problem
Generate the Fibonacci series up to a given number of terms.

In a Fibonacci series, each number is the sum of the previous two numbers.

---

## Example

Input:
```python
terms = 7
```

Output:
```python
0 1 1 2 3 5 8
```

Explanation:
```python
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
```

---

## Python Code

```python
def fibonacci(terms):
    a = 0
    b = 1

    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b


terms = 7

fibonacci(terms)
```

---

## Simple Explanation

- Start with 0 and 1.
- Print the first number.
- Add the previous two numbers to get the next number.
- Repeat until the required number of terms is generated.

---

## Time Complexity
```python
O(n)
```

where `n` is the number of terms.

---

## Commit Message

```bash
Day 25: Generated Fibonacci series using Python
```
