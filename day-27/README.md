# Day 27 

## ⭐️ Relative Ranks – 27.1
### 🔗 Problem
[LeetCode #506 – Relative Ranks](https://leetcode.com/problems/relative-ranks/)

### 🧠 Core Idea
Pair each score with its original index, sort scores in descending order, and assign medals to the top three athletes ("Gold Medal", "Silver Medal", "Bronze Medal").
For the remaining athletes, assign their rank number as a string.
Place the results back into their original positions to preserve input order.

### 📊 Example
Input: `score = \[10,3,8,9,4]`

Output: \["Gold Medal","5","Bronze Medal","Silver Medal","4"]

### ⏱️ Complexity
- Time: O(n log n) – Sorting the scores

- Space: O(n) – For the result array and index pairs

👉 See full code in [relative_ranks.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-27/relative_ranks.py)

---

## ⭐️ Find the Difference – 27.2
### 🔗 Problem
[LeetCode #389 – Find the Difference](https://leetcode.com/problems/find-the-difference/)

### 🧠 Core Idea
The extra character in string `t` can be found by XORing all characters in `s` and `t`. Matching characters cancel out, leaving only the added character.
Alternatively, compute the difference of ASCII sums of `t` and `s`.
Both methods work in linear time and constant space.

### 📊 Example
Input: s = "abcd", t = "abcde"

Output: "e" → Because "e" is the extra character in `t`

### ⏱️ Complexity
- Time: O(n) – One pass through both strings

- Space: O(1) – Only a few variables used

👉 See full code in [find_the_difference.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-27/find_the_difference.py)
