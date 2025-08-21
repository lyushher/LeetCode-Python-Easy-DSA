# Day - 23 
## ⭐️ Path Sum – 23.1
### 🔗 Problem
[LeetCode #112 – Path Sum](https://leetcode.com/problems/path-sum/)

### 🧠 Core Idea
Check if there exists a root-to-leaf path whose node values sum up to the given target. Recursively subtract the current node’s value from the target and move down. If a leaf node is reached and the remaining target equals the leaf’s value, return true. Otherwise, continue searching left and right.

### 📊 Example
Input: root = \[5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

Output: true -> Path 5 -> 4 -> 11 -> 2 adds up to 22.

### ⏱️ Complexity
- Time: O(n) – Each node is visited once

- Space: O(h) – Recursion stack, h = tree height

👉 See full code in [path_sum.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-23/path_sum.py)

---

## ⭐️ Balanced Binary Tree – 23.2
### 🔗 Problem
[LeetCode #110 – Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

### 🧠 Core Idea
A binary tree is balanced if for every node, the heights of its left and right subtrees differ by at most 1. Perform a bottom-up DFS that computes subtree heights while checking balance. If any imbalance is found, propagate it upward immediately. Otherwise, return `1 + max(left_height, right_height)` for each node.

### 📊 Example
Input: root = \[3,9,20,null,null,15,7]

Output: true -> Both subtrees of every node differ in height by at most 1.

### ⏱️ Complexity
- Time: O(n) – Each node visited once

- Space: O(h) – Recursion stack, h = tree height

👉 See full code in [balanced_binary_tree.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-23/path_sum.py)
