class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:

    # adjacency list and count of available flights from src to dest
    self.remaining = collections.defaultdict(int)
    self.adj_list = collections.defaultdict(list)
    for src,dest in tickets:
      self.adj_list[src].append(dest)
      self.remaining[(src,dest)] += 1

    # sort lexicographically for tie-breaking
    for _,adj in self.adj_list.items():
      adj.sort()

    def loop(cur: str, output: List[str]):
      output.append(cur)

      # if this airport is a dead end, stop recursing
      if len(self.adj_list[cur]) == 0:
        if len(output) == len(tickets)+1:
          return output
        else:
          output.pop()
          return None

      # we've used all tickets, bubble answer to top
      if len(output) == len(tickets)+1:
          return output

      # loop through all available flights from current airport
      for adj in self.adj_list[cur]:
        if self.remaining[(cur,adj)] > 0:
          self.remaining[(cur,adj)] -= 1
          l = loop(adj, output)
          if l != None: return l # we've found an answer, bubble it to the top
          self.remaining[(cur,adj)] += 1

      # this airport did not lead to a solution, pop from output
      output.pop()

    # run driver
    return loop("JFK", [])
