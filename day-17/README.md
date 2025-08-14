# Day - 17
## ⭐️ Find Smallest Letter Greater Than Target – 17.1
### 🔗 Problem

[LeetCode #744 – Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)
### 🧠 Core Idea

We apply binary search to locate the smallest letter in a sorted list that is strictly greater than the target character. 
If such a letter exists, it is returned immediately. 
If all letters are less than or equal to the target, we wrap around and return the first element of the list. 
This approach leverages the sorted order to achieve O(log n) search time.

### 📊 Example

Input: `letters = ["c","f","j"]`, `target = "a"`

Output: "c" -> "c" is the smallest letter greater than "a".

### ⏱️ Complexity

- Time: O(log n) – Binary search halves the range each step

- Space: O(1) – Only a few variables are used

👉 See full code in [find_smallest_letter_greater_than_target.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-17/find_smallest_letter_greater_than_target.py)

---

## ⭐️ Guess Number Higher or Lower – 17.2
### 🔗 Problem

[LeetCode #374 – Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

### 🧠 Core Idea

We use binary search between 1 and n to minimize the number of guesses. On each iteration, we guess the midpoint and use the provided API guess(num) to check:

- If it returns 0, we found the target.
- If it returns -1, the target is smaller, so we move the right bound to mid - 1.
- If it returns 1, the target is larger, so we move the left bound to mid + 1.
- This approach guarantees logarithmic search time in the worst case.

### 📊 Example
Input: `n = 10`, `pick = 6`

Output: 6 -> Found in minimal guesses.

### ⏱️ Complexity

- Time: O(log n) – Range halved each iteration

- Space: O(1) – Constant extra variables

👉 See full code in [guess_number_higher_or_lower.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-17/guess_number_higher_or_lower.py)
