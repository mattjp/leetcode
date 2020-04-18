class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    first_ptr = head
    second_ptr = head
    count = 1
    while first_ptr.next is not None:
      first_ptr = first_ptr.next
      count += 1
    half = count // 2
    for i in range(0, half):
      second_ptr = second_ptr.next
    return second_ptr
