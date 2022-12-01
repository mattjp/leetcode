/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
  
  private List<int> Helper(TreeNode node, List<int> vals) {
    if (node == null) {
      return vals;
    }
    
    vals.Add(node.val);
    Helper(node.left, vals);  // List is pass by reference
    Helper(node.right, vals); // Could also do vals = ... to set explicitly
    return vals;
  }
  
  
  public IList<int> PreorderTraversal(TreeNode root) {
    return Helper(root, new List<int>());
  }
}
