# Day - 11
## ⭐️ Reverse Linked List – 11.1
### 🔗 Problem
[LeetCode #206 – Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

### 🧠 Core Idea
Iteratively reverse the list by reassigning next pointers as we traverse.
Keep track of the previous node while moving through the list to reverse links in place.
This approach avoids recursion, reducing memory usage and preventing stack overflow in large lists.

### 📊 Example
Input: 1 -> 2 -> 3 -> 4 -> 5

Output: 5 -> 4 -> 3 -> 2 -> 1

### ⏱️ Complexity
- Time: O(n) – Single pass over the list

- Space: O(1) – No extra storage needed

👉 See full code in [reverse_linked_list.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-11/reverse_linked_list.py)

---

## ⭐️ Merge Two Sorted Lists – 11.2
### 🔗 Problem
[LeetCode #21 – Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

### 🧠 Core Idea
Use a dummy head and tail pointer to merge two sorted linked lists in ascending order.
Compare the heads of both lists, attaching the smaller node to the merged list, then advance pointers accordingly.
Finish by attaching any remaining nodes from either list.

### 📊 Example
Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4

Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

### ⏱️ Complexity
- Time: O(n + m) – Traverse both lists fully

- Space: O(1) – Merged in place using pointers

👉 See full code in [merge_two_sorted_lists.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-11/merge_two_sorted_lists.py)
