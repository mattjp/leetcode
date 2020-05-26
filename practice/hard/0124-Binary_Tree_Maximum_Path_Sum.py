class Solution:
  def maxPathSum(self, root: TreeNode) -> int:
    # save global max
    # for each node -> add left tree sum + val + right tree sum
    # if larger, save as global max

    self.global_max = None

    def loop(root: TreeNode) -> int:
        if root == None:
          return 0
          
        # get max for left and right sub-trees
        l = loop(root.left) 
        r = loop(root.right)
        
        # if sub-tree was negative, ignore it as it won't ever make the global max larger
        l = 0 if l < 0 else l 
        r = 0 if r < 0 else r
        
        # the best we can do for any given node is the sum of itself and its sub-trees
        cur_max = l + r + root.val
        if self.global_max == None or cur_max > self.global_max:
            self.global_max = cur_max
            
        # return the max path path through the root
        # only one sub-tree is returned because a path can only have one "turn-around" node
        return max(l,r) + root.val

    loop(root)
    return self.global_max
