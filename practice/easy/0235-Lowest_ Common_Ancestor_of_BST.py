class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    if p > n and q < n then n must be LCA
    if either p==n or q==n then n must be LCA
    if both p>n,q>n or vice versa, recurse that direction
    """
    def search(node: TreeNode, p: TreeNode, q: TreeNode):
      if ( # check all node conditions
        node == p or
        node == q or
        (p.val > node.val and q.val < node.val) or
        (p.val < node.val and q.val > node.val)
      ):
        return node
      
      # at this point, both p and q must be greater than or less than node
      if p.val < node.val and q.val < node.val:
        return search(node.left, p, q)
      else:
        return search(node.right, p, q)

    return search(root, p, q)
