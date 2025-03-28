# Two Sum

![Status: Solved](https://img.shields.io/badge/Status-Solved-brightgreen) ![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-blue)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

### Rules:
- Each input has **exactly one solution**.
- You **cannot use the same element twice**.
- The answer can be returned **in any order**.

---

## Examples

### Example 1:
**Input:**  
```python
nums = [2,7,11,15]
target = 9
```
**Output:**  
```python
[0, 1]
```
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`, so we return `[0, 1]`.

---

### Example 2:
**Input:**  
```python
nums = [3,2,4]
target = 6
```
**Output:**  
```python
[1, 2]
```

---

### Example 3:
**Input:**  
```python
nums = [3,3]
target = 6
```
**Output:**  
```python
[0, 1]
```

---

## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

---

## Follow-up
Can you design an **algorithm with less than O(n²) time complexity**? 🤔

---

## Solution
Check out the solution in the [`twoSum.py`](./twoSum.py) file. 🚀

