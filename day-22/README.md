# Day - 22
## ⭐️ Symmetric Tree – 22.1
### 🔗 Problem

[LeetCode #101 – Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

### 🧠 Core Idea

A tree is symmetric if it is a mirror of itself, which means the left subtree is a mirror reflection of the right subtree. We compare nodes in pairs: both null implies a match, one null or unequal values implies asymmetry, otherwise we recursively check the outer pair (left.left vs right.right) and the inner pair (left.right vs right.left) to ensure full mirrored structure and values.

### 📊 Example

Input: `root = [1,2,2,3,4,4,3]`

Output: true

### ⏱️ Complexity

- Time: O(n) – Each node visited once

- Space: O(h) – Recursion stack, h = tree height

👉 See full code in [symmetric_tree.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-22/symmetric_tree.py)

---

## ⭐️ Invert Binary Tree – 22.2
### 🔗 Problem

[LeetCode #226 – Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)_

### 🧠 Core Idea

Inversion creates the mirror image of a binary tree by swapping the left and right child at every node. Using DFS, we swap children at the current node and recurse into both subtrees; an empty node returns immediately. The result is the original tree reflected across its root.

### 📊 Example

Input: `root = [4,2,7,1,3,6,9]`

Output: [4,7,2,9,6,3,1]

### ⏱️ Complexity

- Time: O(n) – Visit and swap at each node once

- Space: O(h) – Recursion stack, h = tree height

👉 See full code in [invert_binary_tree.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-22/invert_binary_tree.py)
