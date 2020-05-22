# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = None
    tail = head
    carry = 0

    while l1 != None and l2 != None:
      val = l1.val + l2.val + carry
      carry = val // 10
      val %= 10
      if head == None:
        head = ListNode(val)
        tail = head
      else:
        tail.next = ListNode(val)
        tail = tail.next
      l1 = l1.next
      l2 = l2.next

    # this logic is dumb and redundant 
    while l1 != None:
      val = l1.val + carry
      carry = val // 10
      val %= 10
      tail.next = ListNode(val)
      tail = tail.next
      l1 = l1.next

    while l2 != None:
      val = l2.val + carry
      carry = val // 10
      val %= 10
      tail.next = ListNode(val)
      tail = tail.next
      l2 = l2.next

    if carry == 1:
      tail.next = ListNode(1)

    return head
