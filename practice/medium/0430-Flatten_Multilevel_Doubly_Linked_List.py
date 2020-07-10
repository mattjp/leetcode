"""
# Definition for a Node.
class Node:
def __init__(self, val, prev, next, child):
  self.val = val
  self.prev = prev
  self.next = next
  self.child = child
"""

class Solution:
  def flatten(self, head: 'Node') -> 'Node':
    """
    for each node
    add to result list
    if there is a child recurse -> return head
    """

    def add_list(node: 'Node'):
      head = Node() # start one behind head in case head has a child
      prev_itr = head # `prev_itr` will track the last node added to the NEW list
      itr = node # `itr` will go through the original list one-by-one

      while itr:
        # make copy of current node, link forward and backward with `prev_itr`
        cur = Node(itr.val)
        cur.prev = prev_itr
        prev_itr.next = cur

        if itr.child:
          # recurse if a child exists
          # `child_head` and `child_tail` will be NEW nodes
          child_head, child_tail = add_list(itr.child)

          # `child_tail` must be linked to `itr.next`, if it exists
          # this will continue iterating as usual
          if itr.next:
            tmp_node = Node(itr.next.val)
            tmp_node.prev = child_tail
            child_tail.next = tmp_node

          # `child_head` must be linked with `prev_itr`
          cur.next = child_head
          child_head.prev = cur

          # jump `prev_itr` forward to the new "last" node added to the NEW list
          prev_itr = child_tail
        else:
          prev_itr = prev_itr.next

        itr = itr.next # always increment `itr`

      if head.next: head.next.prev = None # make prev must be None to be valid linkage
      return (head.next, prev_itr) # return head and tail in order to link properly

    # return list head only
    return add_list(head)[0]
