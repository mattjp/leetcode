# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        output = []
        while queue:
          top = queue.popleft()
          if top:
            output.append(str(top.val))
            queue.append(top.left)
            queue.append(top.right)
          else:
            output.append('null')

        return ','.join(output)
        

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split(','))
        
        top = queue.popleft()
        if top == 'null':
          return None
        
        root = TreeNode(top)
        row = [root]

        while queue:
          cur = row.pop(0)
          l = queue.popleft()
          r = queue.popleft()
          
          lt = TreeNode(l) if l != None else None
          rt = TreeNode(r) if r != None else None
            
          cur.left = lt
          cur.right = rt

          if lt != None:
            row.append(cur.left)
          if rt != None:
            row.append(cur.right)

        return root  

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
