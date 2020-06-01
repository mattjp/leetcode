class Solution:
  def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
    from collections import defaultdict

    # create adjacency list for both nodes in the edge
    adj_list = defaultdict(list)
    for u,v in dislikes:
      adj_list[u].append(v)
      adj_list[v].append(u)

    colors = defaultdict()
    
    # given a person, return true if they have a different color than their neighbors
    def can_color(person: int, color: int) -> bool:
      # make sure the neighbor color is the same as what has already been assigned
      if person in colors:
        return colors[person] == color
      colors[person] = color
      return all([can_color(p, color * -1) for p in adj_list[person]])

    # check if all persons can be divided into 2 colors
    for n in range(N):
      # if the person `n` is not in the adjacency list, they can be either color safely
      if n in adj_list:
        c = colors[n] if n in colors else 1
        if not can_color(n, c):
          return False
    return True
