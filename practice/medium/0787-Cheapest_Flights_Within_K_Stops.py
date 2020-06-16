class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    """
    if adding another flight >K, return
    if adding this flight is going to be more expensive than `best` return
    if the destination is in the adj_list of this flight, update `best` if necessary
    add the current destination to the set of `seen` flights
    recurse for all flights in the adj_list
    when coming out of recursive call, remove the city from seen
    """
        
    self.best = None
    self.seen = set()
    adj_list = collections.defaultdict(list)
    prices = {}
        
    # graph is directed and weighted
    for f1,f2,p in flights:
      adj_list[f1].append(f2)
      prices[(f1,f2)] = p
          
    # DFS every airport until you find the target, or k > K
    def find_path(cur_city: int, cur_k: int, cur_price: int) -> None:
      # too many stops
      if cur_k > K:
        return
          
      # don't cycle through airports
      self.seen.add(cur_city)
          
      # try all connecting airports
      for adj in adj_list[cur_city]:
        # except if we've seen that airport before
        if adj not in self.seen:
          # total cost              
          adj_price = cur_price + prices[(cur_city, adj)]
          # if this is the target save best price
          if adj == dst:
            self.best = adj_price if self.best == None else min(self.best, adj_price)
          # otherwise keep looking
          elif self.best == None or adj_price < self.best:
            find_path(adj, cur_k+1, adj_price)
                
      # once we've searched all adjacent cities, remove the current one from seen
      self.seen.remove(cur_city)
          
    # call the driver function
    find_path(src, 0, 0)
    return self.best if self.best != None else -1
