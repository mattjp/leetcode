class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

    adj_mat = collections.defaultdict(list)
    for i,g in enumerate(graph): 
      adj_mat[i] = g

    self.target = len(graph)-1

    def find_path(cur_node: int=0, cur_path: List[int]=[], output: List[List[int]]=[]):
      cur_path.append(cur_node)

      if cur_node == self.target:
        output.append(cur_path.copy())
        cur_path.pop()
        return output

      for adj_node in adj_mat[cur_node]:
        output = find_path(adj_node, cur_path, output)

      cur_path.pop()
      return output

    return find_path()
