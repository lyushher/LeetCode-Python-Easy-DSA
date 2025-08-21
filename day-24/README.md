# Day - 24

## ⭐️ Minimum Depth of Binary Tree – 24.1
### 🔗 Problem
[LeetCode #111 – Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

### 🧠 Core Idea
To find the shortest path from root to the nearest leaf, recursively check both subtrees. If one child is missing, we must take the non-null path. If both exist, choose the smaller of the two depths. Always add 1 for the current node.

### 📊 Example
Input: `root = \[3,9,20,null,null,15,7]`

Output: 2 -> Because the minimum path is 3 -> 9

### ⏱️ Complexity
- Time: O(n) – Visit each node once

- Space: O(h) – Recursion stack, h = height of tree

👉 See full code in [minimum_depth_binary_tree.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-24/minimum_depth_of_binary_tree.py)

---

## ⭐️ Range Sum of BST – 24.2
### 🔗 Problem
[LeetCode #938 – Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/description/)

### 🧠 Core Idea
Leverage BST properties to prune traversal. If node value < low, skip the left subtree. If node value > high, skip the right subtree. Otherwise, add the node’s value and continue to both children. This way we avoid exploring irrelevant branches.

### 📊 Example
Input: `root = \[10,5,15,3,7,null,18]`, low = 7, high = 15

Output: 32 -> Because values 7 + 10 + 15 = 32 fall within the range

### ⏱️ Complexity
- Time: O(m), where m is number of visited nodes (≤ n)

- Space: O(h), recursion stack depth

👉 See full code in [range_sum_of_bst.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-24/range_sum_of_bst.py)
