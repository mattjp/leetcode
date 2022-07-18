# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        cur = head.next
        prev = head
        
        while cur != None:
            while cur != None and cur.val == prev.val:
                cur = cur.next
            
            prev.next = cur
            prev = cur
            cur = cur.next if cur != None else None
            
        return head
