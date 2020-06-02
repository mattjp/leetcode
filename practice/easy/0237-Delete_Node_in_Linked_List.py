class Solution:
  def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    set the target nodes value to the next value, then skip the next node
    """
    node.val = node.next.val
    node.next = node.next.next
