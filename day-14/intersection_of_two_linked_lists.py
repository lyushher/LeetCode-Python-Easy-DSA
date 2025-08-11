# Problem: Intersection of Two Linked Lists
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Tags: Linked List, Two-Pointer
# Approach: Two-pointer switching – traverse both lists, and when one pointer reaches the end, 
#           redirect it to the head of the other list. This way, both pointers travel equal total distance.
#           If there's an intersection, they'll meet at the intersection node; otherwise, both reach None.
# Time Complexity: O(n + m) – Each list traversed at most twice
# Space Complexity: O(1) – Only pointer variables used

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA  # either intersection node or None

