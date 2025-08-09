# Problem: Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/description/
# Tags: Linked List, Two-Pointer, Reverse, Fast and Slow Pointers
# Approach: Use fast & slow pointers to find the midpoint, reverse the second half, and compare both halves
# Time Complexity: O(n) 
# Space Complexity: O(1) 


class Solution:
    def isPalindrome(self, head):
        # find the middle of the linked list using fast & slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # compare the first half and the reversed second half
        left, right = head, prev
        while right:  # right will be shorter or equal in length
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # if all nodes matched, it's a palindrome
        return True
