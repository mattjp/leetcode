# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1. get length of list, l
        2. find new head, nh=(k%l).next
        3. node pointing to new head now points to null
        4. last node pointing to original head
        5. return new head
        """
        
        def get_len(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l
        
        l = get_len(head)
        if l == 0 or l == 1:
            return head
        
        new_head_index = (l - (k % l)) % l
        
        if new_head_index == 0:
            return head
        
        new_head = head
        for i in range(new_head_index-1):
            new_head = new_head.next
            
        ret_head = new_head.next
        new_head.next = None
        
        itr = ret_head
        while itr.next:
            itr = itr.next
            
        itr.next = head
        return ret_head
