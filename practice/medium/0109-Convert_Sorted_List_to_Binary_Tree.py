# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    """
    let's just always insert the middle and then recurse
    idea is there, just no need for bst_insert since you know the middle
    is the next element to insert
    """
    def bst_insert(node, v): # this is dumb, you already know where to go
      if not node:
        return TreeNode(v)
      if node.val > v:
        node.left = bst_insert(node.left, v)
      elif node.val < v:
        node.right = bst_insert(node.right, v)
      return node
      
    def find_insert_middle(ls):
      if not ls:
        return
      m = len(ls)//2
      self.root = bst_insert(self.root, ls[m])
      find_insert_middle(ls[:m])
      find_insert_middle(ls[m+1:])
      
      
    ls = []
    while head:
      ls.append(head.val)
      head = head.next
      
    self.root = None
    find_insert_middle(ls)
    return self.root
