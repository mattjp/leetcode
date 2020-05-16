# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
      return head

    odd = head
    odd_head = odd
    even = head.next
    even_head = even
    while odd.next is not None and even.next is not None: # odd.next fails before even.next so no exceptions
      odd.next = even.next
      odd = odd.next
      even.next = odd.next
      even = even.next

    odd.next = even_head # set end of odd list equal to start of even list
    return odd_head
