# Day 1 - Two Sum

## Problem
Given a list of numbers and a target number, find the two numbers that add up to the target and return their index positions.

You cannot use the same number twice.

---

## Example

Input:
```python
nums = [2, 7, 11, 15]
target = 9
```

Output:
```python
[0, 1]
```

Explanation:
```python
2 + 7 = 9
```

So the answer is index `0` and index `1`.

---

## Python Code

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
```

---

## Simple Explanation

- Go through each number one by one.
- Find what number is needed to make the target.
- Check if that needed number was already seen before.
- If yes, return both index positions.
- Store current number in dictionary.

---

## Time Complexity
```python
O(n)
```

---

## Commit Message
```bash
Day 1: Solved Two Sum problem in Python
```
