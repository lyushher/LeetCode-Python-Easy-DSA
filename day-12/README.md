# Day - 12

## ⭐️ Palindrome Linked List – 12.1

### 🔗 Problem
[LeetCode #234 – Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

### 🧠 Core Idea
Find the middle of the linked list using the fast/slow pointer method.
Reverse the second half in-place, then compare the first half and reversed second half node by node.

### 📊 Example
Input: head = [1, 2, 2, 1]

Output: true → Reads the same forward and backward.

### ⏱️ Complexity
- Time: O(n) – Single pass to find the middle and compare.

- Space: O(1) – Reversing in-place avoids extra memory usage.

👉 See full code in [palindrome_linked_list.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-12/palindrome_linked_list.py)

---

## ⭐️ Linked List Cycle – 12.2

### 🔗 Problem
[LeetCode #141 – Linked List Cycle](https://leetcode.com/problems/palindrome-linked-list/)

### 🧠 Core Idea
Use two pointers moving at different speeds (slow: +1 step, fast: +2 steps).
If they ever meet, a cycle exists. If the fast pointer reaches the end, no cycle exists.
This is the Floyd’s Tortoise and Hare approach.

### 📊 Example
Input: `head = [3, 2, 0, -4]`, `pos = 1`

Output: true → The last node links back to the node at index 1.

### ⏱️ Complexity
- Time: O(n) – Each pointer traverses the list at most once.

- Space: O(1) – No extra data structures used.

👉 See full code in [linked_list_cycle.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-12/linked_list_cycle.py)
