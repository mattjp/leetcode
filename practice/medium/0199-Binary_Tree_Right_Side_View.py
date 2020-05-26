class Solution:
  def rightSideView(self, root: TreeNode) -> List[int]:
    # do BFS
    # save last node seen for each depth-level of tree

    if root == None:
      return []

    output = []
    stack = [root]

    while len(stack) > 0:
      children = [] # reset new BFS row
      while len(stack) > 0:
        top = stack.pop(0)
        if top.left != None:
          children.append(top.left)
        if top.right != None:
          children.append(top.right)
        if len(stack) == 0: # add the last child element
          output.append(top.val)
          
      # copy over new row of tree nodes
      stack = children

    return output
