"""
# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
      self.val = int(x)
      self.next = next
      self.random = random
"""

class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':

    # dumb
    if head == None:
      return None

    # old_node -> new_node
    mapping = {} 

    # iterate 2 pointers at a time until forward pointer is None
    itr1 = head
    itr2 = head.next
    while itr2 != None:
      # create new temporary node for forward pointer
      node2 = Node(itr2.val)
      # create new node for backward pointer using forward pointer
      node1 = Node(itr1.val, node2)
      # save mapping for backward pointer (old node -> new node)
      mapping[itr1] = node1
      # iterate
      itr1 = itr1.next
      itr2 = itr2.next

    # handle the last node before end-of-list
    mapping[itr1] = Node(itr1.val)

    # update mapping with random pointers
    itr1 = head
    while itr1 != None:
      if itr1.random != None:
        # if there is a random pointer, find the new copy using the old pointer
        mapping[itr1].random = mapping[itr1.random]
      itr1 = itr1.next

    # create new list using mapping
    itr1 = head
    copy_head = Node(0)
    copy_itr = copy_head
    while itr1 != None:
      copy_itr.next = mapping[itr1]
      copy_itr = copy_itr.next
      itr1 = itr1.next

    return copy_head.next
