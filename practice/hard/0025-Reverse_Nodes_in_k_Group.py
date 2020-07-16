# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    """
    use a left (L) and right (R) pointer
    iterate the right pointer `k` times, then reverse the list from L to R
    rewire the newly reversed list segment
    jump L to R and repeat
    """
    
    def reverse_list_limited(R: ListNode, L: ListNode, stop: ListNode):
      """
      reverse a linked list starting at node `L` until node `stop` is reached
      return the head and tail of the reversed list
      """
      if R == stop: # handles the case of reversing groups of length 1
        return L, L
      
      if R.next == stop: # standard base case, reverses the final 2 nodes
        R.next = L
        L.next = None
        return R, L
      
      # recurse until we hit the `stop` node, then we'll have the head of the new list
      head, _ = reverse_list_limited(R.next, L.next, stop)
      
      # reverse right iterator to point left, left points to EOL
      R.next = L
      L.next = None
      
      # return new head and left iterator (tail)
      return head, L
    

    output = ListNode(-1, head) # node that points at the head of the list so reversing works for the first group of `k` nodes
    L_prev = output # remember what points to L for rewiring
    R = head
    L = head
    i = 0
    
    while R:
      i += 1
      R = R.next
      if i % k == 0: # we have a group of length `k` to be reversed
        L_rev, R_rev = reverse_list_limited(L.next, L_prev.next, R)
        L = R               # jump `L` to `R`
        L_prev.next = L_rev # rewire left-hand side
        L_prev = R_rev      # jump `L_prev` to the end of the reversed list
        L_prev.next = R     # rewire right-hand side

    return output.next
