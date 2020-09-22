class Solution:
  def insert(self, head: 'Node', insertVal: int) -> 'Node':
    if not head: # handle empty list
      n = Node(insertVal)
      n.next = n
      return n
    
    a = head
    b = head.next 
    while a.val > insertVal or b.val < insertVal: # covers all scenarios where a <= c <= b
      if (
        a.next == head or # put at end-of-list
        (b.val < a.val and (insertVal <= b.val or insertVal >= a.val)) # put at rotation point
      ):
        c = Node(insertVal, b)
        a.next = c
        break
      a = a.next
      b = b.next
    else:
      c = Node(insertVal, b)
      a.next = c

    return head
