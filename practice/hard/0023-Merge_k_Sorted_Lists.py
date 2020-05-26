# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:

    # iterate through all lists
    # add val to priority queue
    # create list based on PQ

    heap = []
    for l in lists:
      while l != None:
        heapq.heappush(heap, l.val)
        l = l.next

    head = None
    tail = head

    while len(heap) > 0:
      v = heapq.heappop(heap)
      if head == None:
        head = ListNode(v)
        tail = head
      else:
        tail.next = ListNode(v)
        tail = tail.next

    return head
