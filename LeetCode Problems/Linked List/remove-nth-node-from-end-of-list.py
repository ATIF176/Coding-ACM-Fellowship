# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps ahead
        for i in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Now, second points to the node just before the one to be removed
        second.next = second.next.next

        return dummy.next


# Example 1:
# Input: head = [1,2,3,4,5], n = 2  
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []