# Problem: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Tags: Linked List, Two-Pointer, Merge
# Approach: Iterative merging with a dummy head
# Time Complexity: O(n + m) – Traverse both lists fully
# Space Complexity: O(1) – No extra structures (only pointers)


class Solution:
    def mergeTwoLists(self, list1, list2):
        # dummy node to simplify edge cases
        dummy = ListNode()
        tail = dummy  # tail pointer to build the merged list

        # traverse both lists while elements remain
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # attach smaller node
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # move tail forward

        # attach the remaining nodes from either list
        tail.next = list1 or list2

        # the merged list starts from dummy.next
        return dummy.next
