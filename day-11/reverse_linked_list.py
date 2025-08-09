# Problem: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/description/
# Tags: Linked List, Iteration, Two-Pointer
# Approach: Iterative pointer reversal
# Time Complexity: O(n) – Each node is visited once
# Space Complexity: O(1) – No extra data structures used


class Solution:
    def reverseList(self, head):
        prev = None    # initially, previous node is None
        curr = head    # start from the head of the list

        # traverse the list
        while curr:
            nxt = curr.next   # store the next node before breaking the link
            curr.next = prev  # reverse the link
            prev = curr       # move 'prev' forward
            curr = nxt        # move 'curr' forward

        # 'prev' will be the new head after the loop
        return prev
