class Solution:
def reverseList(self, head: ListNode) -> ListNode:

  def helper(node: ListNode):
    if node == None or node.next == None:
        return node, node # head and tail will be the same for the final node

    h, t = helper(node.next) # `t` is the next node of `node`
    t.next = node #
    node.next = None
    return h, node # always return `h` because that is the new head

  return helper(head)[0]
