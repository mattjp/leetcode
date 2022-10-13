# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        Node values are unique, so copy the next value into the current node
        For the second to last node, set next = None
        """
        
        ptr = node
        prev = None
        
        while ptr:
            if ptr.next:
                ptr.val = ptr.next.val
                prev = ptr
                ptr = ptr.next
            else:
                prev.next = None
                ptr = None
