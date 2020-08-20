# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head: return

    # map every list node to its index in the linked-list
    index = {}
    itr = head
    i = 0
    while itr:
      index[i] = itr
      i += 1
      itr = itr.next

    # reconstruct the list using the newly created mapping
    length = i
    i = 0
    itr = head
    while i < (length // 2):
      itr.next = index[length-i-1] # current node i next is set to EOL - i
      itr = itr.next 
      i += 1
      itr.next = index[i] # next node is simply i+1
      itr = itr.next

    itr.next = None # set final node to end-of-list
