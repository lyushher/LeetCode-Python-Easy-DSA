# Problem: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/description/
# Tags: Linked List, Two-Pointer, Cycle Detection
# Approach: Floyd's Tortoise and Hare Algorithm
# Time Complexity: O(n) – Each pointer traverses at most n nodes
# Space Complexity: O(1) – Uses only two pointers without extra data structures


class Solution:
    def hasCycle(self, head):
        # initialize two pointers
        slow = head
        fast = head

        # move slow by 1 and fast by 2; if they ever meet, there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        # fast reached the end ⇒ no cycle
        return False
