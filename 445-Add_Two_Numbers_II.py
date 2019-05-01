# 445. Add Two Numbers II
#
# You are given two non-empty linked lists representing two non-negative 
# integers. The most significant digit comes first and each of their nodes 
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the 
# number 0 itself.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    s1, s2 = [], []
    carry = 0
    prev = None

    while l1 is not None:
      s1.append(l1)
      l1 = l1.next

    while l2 is not None:
      s2.append(l2)
      l2 = l2.next

    while len(s1) > 0 and len(s2) > 0:
      x1 = s1.pop()
      x2 = s2.pop()
      y = x1.val + x2.val + carry
      carry = 0
      if y > 9:
        carry = 1
        y %= 10
      l3 = ListNode(y)
      l3.next = prev
      prev = l3

    while len(s1) > 0:
      x1 = s1.pop()
      x1.val += carry
      carry = 0
      if x1.val > 9:
        carry = 1
        x1.val %= 10
      x1.next = prev
      prev = x1

    while len(s2) > 0:
      x2 = s2.pop()
      x2.val += carry
      carry = 0
      if x2.val > 9:
        carry = 1
        x2.val %= 10
      x2.next = prev
      prev = x2

    if carry:
      x3 = ListNode(carry)
      x3.next = prev
      prev = x3

    return prev
