class FileSystem:
  
  class Node:
    def __init__(self):
      self.dirs = {}
      self.files = {}
  
  
  def split_path(self, path: str) -> List[str]:
    """
    split path by '/' and remove empty strs
    """
    dirs = path.split('/')
    return list(filter(lambda x: x!='', dirs))
  

  def __init__(self):
    self.root = FileSystem.Node()


  def ls(self, path: str) -> List[str]:
    dirs = self.split_path(path)
    node = self.root

    for d in dirs[:-1]:
      node = node.dirs[d]

    # this is nasty, but functional
    if not dirs:
      return sorted(list(node.dirs.keys()) + list(node.files.keys()))
    else:
      d = dirs[-1]
      if d in node.files:
        return [d]
      else:
        return sorted(list(node.dirs[d].dirs.keys()) + list(node.dirs[d].files.keys()))


  def mkdir(self, path: str) -> None:
    dirs = self.split_path(path)
    node = self.root
    
    for d in dirs:
      if d not in node.dirs:
        node.dirs[d] = FileSystem.Node()
      node = node.dirs[d]


  def addContentToFile(self, filePath: str, content: str) -> None:
    node = self.root
    path = self.split_path(filePath)
    dirs = path[:-1]
    file = path[-1]
    
    for d in dirs:
      if d not in node.dirs:
        node.dirs[d] = FileSystem.Node()
      node = node.dirs[d]
      
    if file not in node.files:
      node.files[file] = ''
    node.files[file] += content


  def readContentFromFile(self, filePath: str) -> str:
    node = self.root
    path = self.split_path(filePath)
    dirs = path[:-1]
    file = path[-1]
    
    for d in dirs:
      if d not in node.dirs:
        node.dirs[d] = FileSystem.Node()
      node = node.dirs[d]
      
    return node.files[file]
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
