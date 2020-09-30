# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    """
    note: could have also just saved the duplicate value, then iterated,
    rather than comparing node values in place.
    """
    
    head_prev = ListNode(None, head)
    l = head_prev
    r = head
    
    while r:
      dupe = False
      while r.next and r.next.val == r.val:
        r = r.next
        dupe = True
        
      if dupe:
        r = r.next
        l.next = r # note we do not move l ahead, must wait for next iteration
      
      if not dupe:
        l.next = r
        l = l.next
        r = r.next
      
    return head_prev.next
