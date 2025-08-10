# Day - 13
## ⭐️ Delete Node in a Linked List – 13.1
### 🔗 Problem
[LeetCode #237 – Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

### 🧠 Core Idea
Since the node to be deleted is not the tail and we have no access to the head, we copy the value from the next node into the current node and then bypass the next node.
This effectively "deletes" the target node without needing to traverse from the head.

### 📊 Example
Input: 4 -> 5 -> 1 -> 9, node = 5

Output: 4 -> 1 -> 9 - Node 5 is removed by overwriting its value and skipping its next reference.

### ⏱️ Complexity
- Time: O(1) – Constant-time value copy and pointer reassignment

- Space: O(1) – No extra structures used

👉 See full code in [delete_node_linked_list.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-13/delete_node_in_a_linked_list.py)

---

## ⭐️ Remove Duplicates from Sorted List – 13.2
### 🔗 Problem
[LeetCode #83 – Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

### 🧠 Core Idea
In a sorted linked list, duplicates appear consecutively, allowing removal in a single pass.
Compare each node with its next; if equal, skip the duplicate by adjusting pointers, otherwise move forward. This keeps the list sorted and unique without extra space.

### 📊 Example
Input: 1 -> 1 -> 2 -> 3 -> 3

Output: 1 -> 2 -> 3 - All consecutive duplicates removed in-place.

### ⏱️ Complexity
- Time: O(n) – Single traversal of the list

- Space: O(1) – In-place update without extra memory

👉 See full code in [remove_duplicates_sorted_list.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-13/remove_duplicates_from_sorted_list.py)


