# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    # create a node that points at head of list
    # we do this so we can run the same algo for all nodes, including head
    prev = ListNode(val=0, next=head) 
    output = prev
    cur = head

    while cur != None:
      if cur.val == val:
        prev.next = cur.next
      # only increment prev once we've found all consecutive `val`s
      else:
        prev = cur 
      cur = cur.next

    return output.next # return the next node of the initial node pointed at the head
