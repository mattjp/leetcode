# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        O(1) space: Find the middle, reverse the second half, iterate and compare 
        """
        
        def getLength(head):
            length = 0
            ptr = head
            while ptr:
                length += 1
                ptr = ptr.next
            return length
        
        
        def bisect(head, length):
            middle = length // 2
            ptr = head
            for _ in range(middle-1):
                ptr = ptr.next
                
            mid_head = ptr.next
            ptr.next = None
                
            # If there are an odd number of elements, we don't care about the middle one
            if length % 2:
                mid_head = mid_head.next
            return mid_head
        
        
        def reverseList(head):
            if head.next == None:
                return head
            tail = reverseList(head.next)
            
            head.next.next = head
            head.next = None
            
            return tail
            
            
        def compareLists(a, b):
            while a and b:
                if a.val != b.val:
                    return False
                a = a.next
                b = b.next
            return True

        
        length = getLength(head)
        
        if length < 2:
            return True
        
        mid_head = bisect(head, length)
        
        rev_head = reverseList(mid_head)
        
        return compareLists(head, rev_head)
