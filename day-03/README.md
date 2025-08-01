# Day - 03
## ⭐️ Intersection of Two Arrays II – 3.1
### 🔗 Problem
[LeetCode #350 – Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

### 🧠 Core Idea
Use a hash map (Counter) to store the frequency of each element in the smaller array.
Then iterate through the second array, and for each element:
→ If it exists in the hash map with count > 0, append it to result and decrease count.

This approach ensures we count duplicates correctly.

### 📊 Example
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2] → Because 2 appears twice in both arrays

### ⏱️ Complexity
Time: O(n + m) – One pass to build the frequency map, one to scan the second array

Space: O(min(n, m)) – Hash map only for the smaller array

👉 See full code in [`intersection_of_two_arrays_ii.py`](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-03/intersection_of_two_arrays_2.py)

## ⭐️ Majority Element – 3.2
### 🔗 Problem
[LeetCode #169 – Majority Element](https://leetcode.com/problems/majority-element/description/)

### 🧠 Core Idea
Apply the Boyer–Moore Voting Algorithm, which tracks a single candidate element and a counter.
If the counter hits zero, we pick a new candidate.
Since the majority element is guaranteed to appear more than ⌊n / 2⌋ times,
this method always returns the correct answer in a single pass using constant space.

### 📊 Example
Input: nums = [3,2,3]
Output: 3 → Because 3 appears more than ⌊3/2⌋ = 1 time

### ⏱️ Complexity
Time: O(n) – Single pass through the array

Space: O(1) – Only two variables are used (candidate, count)

👉 See full code in [`majority_element.py`](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-03/majority_element.py)

