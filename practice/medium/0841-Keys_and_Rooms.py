class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    """
    rooms is an adjacency matrix
    starting at room 0, add all rooms we can visit to the queue
    if all rooms have been checked off, return True
    """
    from collections import deque
    visited = set([0])
    queue = deque([0])
    
    # catch 1 room with no doors
    if len(visited) == len(rooms):
      return True

    # simple BFS
    # BFS will terminate faster than DFS
    while queue:
      cur = queue.popleft()

      for adj in rooms[cur]:
        if adj not in visited:
          visited.add(adj)
          if len(visited) == len(rooms):
            return True
          queue.append(adj)
        
    return False
