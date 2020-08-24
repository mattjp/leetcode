class Solution:
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)

    self.visited = set()

    # roll as far as possible in a given direction
    def roll(maze, cur, direction):
      i = cur[0]
      j = cur[1]
      while (
        i >= 0 and
        i < len(maze) and
        j >= 0 and
        j < len(maze[0]) and
        maze[i][j] != 1  
      ):
        cur = [i, j]
        i += direction[0]
        j += direction[1]
      return cur


    def search(maze, cur, prev, prev_dir, dest):
      # found the end
      if cur == dest: return True

      # hit the wall
      if cur == prev: return False

      # prevent cycles
      if repr(cur) in self.visited: return False
      else: self.visited.add(repr(cur))

      # search all directions, minus the opposite direction from which we came
      return any([
        search(maze, roll(maze, cur, up),    cur, up,    dest) if prev_dir != down else False,
        search(maze, roll(maze, cur, down),  cur, down,  dest) if prev_dir != up else False,
        search(maze, roll(maze, cur, left),  cur, left,  dest) if prev_dir != right else False,
        search(maze, roll(maze, cur, right), cur, right, dest) if prev_dir != left else False
      ])

    return search(maze, start, None, None, destination)
