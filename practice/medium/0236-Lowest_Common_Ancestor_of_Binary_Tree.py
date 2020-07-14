# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    build new tree that is ONLY the path to the target node
    travel both new trees until nodes are no longer equal
    last equal node is the lowest common ancestor
    """


    def build_array(node: TreeNode, target: TreeNode, output: List[TreeNode]):
      """
      Note that `output` is a mutable list, therefore, it will be passed-by-reference
      """
      if node == target:
        output.append(node)
        return True
      elif node == None:
        return False

      output.append(node)

      if any([build_array(node.left, target,output), build_array(node.right, target,output)]):
        return True
      else:
        output.pop()
        return False

    outputp = []
    outputq = []
    build_array(root, p, outputp)
    build_array(root, q, outputq)

    lca = None
    for i in range(min(len(outputp), len(outputq))):
      if outputp[i] == outputq[i]: lca = outputp[i]
      else: return lca
    return lca
