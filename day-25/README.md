# Day 25 

## ⭐️ Count Complete Tree Nodes – 25.1
### 🔗 Problem
[LeetCode #222 – Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

### 🧠 Core Idea
A complete binary tree can be counted more efficiently than traversing all nodes by exploiting its structure. 
At each node, compute the height of the left and right subtrees. 
If they are equal, the left subtree is a perfect binary tree, so its size is 2^h - 1, and the count continues recursively on the right subtree. 
If they differ, then the right subtree is perfect, and recursion continues on the left subtree. 
This divide-and-conquer approach avoids traversing entire subtrees when they are guaranteed to be full.

### 📊 Example
Input: root = [1,2,3,4,5,6]

Output: 6 -> The tree is complete with all nodes filled except possibly the last level.

### ⏱️ Complexity
- Time: O((log n)²) – Each level computes subtree heights in O(log n), repeated across log n levels

- Space: O(log n) – Recursion stack equal to tree height

👉 See full code in [count_complete_tree_nodes.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-25/count_complete_tree_nodes.py)

---

## ⭐️ Leaf-Similar Trees – 25.2
### 🔗 Problem
[LeetCode #872 – Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)

### 🧠 Core Idea
Two binary trees are leaf-similar if their leaf value sequences (from left to right) are identical.
Perform DFS on each tree, collecting values only when visiting a leaf node (no children). After traversal, compare the two sequences.
If they match, the trees are leaf-similar regardless of internal structure.

### 📊 Example
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],  root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

Output: true → Both have leaf sequence [6,7,4,9,8].

### ⏱️ Complexity
- Time: O(n + m) – Each tree fully traversed once

- Space: O(h1 + h2) – Recursion stack proportional to each tree’s height (plus leaf lists)

👉 See full code in [leaf_similar_trees.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-25/leaf_similar_trees.py)
