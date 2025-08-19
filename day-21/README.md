# Day - 21
## ⭐️ Maximum Depth of Binary Tree – 21.1
### 🔗 Problem

[LeetCode #104 – Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### 🧠 Core Idea

The depth of a binary tree is the length of the longest path from the root down to a leaf.
Using recursion (DFS), we return 1 + max(depth(left), depth(right)) for each node.
Base case: if the node is None, depth is 0. This ensures each node is visited once,
and the final result is the maximum depth of the tree.

### 📊 Example

Input: root = [3,9,20,null,null,15,7]

Output: 3 -> Longest path is 3 -> 20 -> 15 or 3 -> 20 -> 7.

### ⏱️ Complexity

- Time: O(n) – Each node is visited once

- Space: O(h) – Recursion stack, h = tree height

👉 See full code in [maximum_depth_of_binary_tree.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-21/maximum_depth_of_binary_tree.py)

---

## ⭐️ Same Tree – 21.2
### 🔗 Problem

[LeetCode #100 – Same Tree](https://leetcode.com/problems/same-tree/)

### 🧠 Core Idea

Two trees are considered the same if they are structurally identical and their corresponding nodes contain the same values. The check is performed by traversing both trees simultaneously: when both nodes are null they match, if only one is null or their values differ they do not match, and otherwise the algorithm recursively compares their left and right subtrees to ensure complete equality in structure and values.

### 📊 Example

Input: p = [1,2,3], q = [1,2,3]

Output: true

### ⏱️ Complexity

- Time: O(n) – Each node compared once

- Space: O(h) – Recursion stack or queue space

👉 See full code in [same_tree.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-21/same_tree.py)
