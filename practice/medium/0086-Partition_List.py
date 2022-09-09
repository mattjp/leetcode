# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Iterate through the original list
        Create 1 list of nodes less than x
        Create 1 list of nodes greater than x
        Concatenate the lists
        """
        
        lt = ListNode()
        gt = ListNode()
        
        lptr = lt
        gptr = gt
        
        hptr = head
        while hptr != None:
            if hptr.val < x:
                lptr.next = hptr
                lptr = lptr.next
            else:
                gptr.next = hptr
                gptr = gptr.next
            hptr = hptr.next
            
            
        gptr.next = None
        lptr.next = gt.next
        
        return lt.next
