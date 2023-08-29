# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        
        # Find the middle element of the linked list
        mid_node = self.find_middle(head)
        
        # Create the root node using the middle element
        root = TreeNode(mid_node.val)
        
        # Recursively build left and right subtrees
        if head == mid_node:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid_node.next)
        
        return root
    
    def find_middle(self, head):
        prev_ptr = None
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        if prev_ptr:
            prev_ptr.next = None
        
        return slow_ptr


# example 1
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
output = Solution().sortedListToBST(head)
print(output)

