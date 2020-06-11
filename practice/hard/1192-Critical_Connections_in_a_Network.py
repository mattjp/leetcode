class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    self.inc = 0
    self.parent = [None] * n
    self.low = [float('inf')] * n # lowest node seen during DFS
    self.disc = [None] * n # order in which nodes are discovered (monotonically increasing)
    self.visited = [False] * n      
    self.res = []
    adj_list = collections.defaultdict(list)

    # standard adjacency list
    for u,v in connections:
      adj_list[u].append(v)
      adj_list[v].append(u)

    def loop(current):
      # do all the node discovery work
      self.visited[current] = True
      self.disc[current] = self.inc
      self.low[current] = self.inc
      self.inc += 1

      # explore all adjacent nodes
      for adj in adj_list[current]:
        # only look at nodes 1 time
        if not self.visited[adj]:
          self.parent[adj] = current
          loop(adj) # recurse to child node

          self.low[current] = min(self.low[current], self.low[adj]) # find reachable node with lowest id

          # if these 2 nodes are parts of different cycles, they aren't strongly-connected
          if self.low[adj] > self.disc[current]:
            self.res.append([current, adj])

        # if we have been to this node (and it's not the parent)
        # check if it has an id lower than the lowest id we've seen so far
        elif self.parent[current] != adj:
          self.low[current] = min(self.low[current], self.disc[adj])

    # detect all cycles
    for i in range(n):
      if not self.visited[i]:
        loop(i)

    return self.res
