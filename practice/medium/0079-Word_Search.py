class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    self.max_i = len(board)
    self.max_j = len(board[0])

    # loop -> checks adjacent cells, recursive
    def loop(board, i: int, j: int, w: int, word: str, checked) -> bool:
      if w == len(word):
          return True

      # do all bounds checking
      if i >= self.max_i \
      or i < 0 \
      or j >= self.max_j \
      or j < 0 \
      or board[i][j] != word[w] \
      or (i,j) in checked:
        return False

      # don't re-use cells
      checked.add((i,j))

      # check all directions
      found = loop(board, i+1, j, w+1, word, checked) \
      or loop(board, i-1, j, w+1, word, checked) \
      or loop(board, i, j+1, w+1, word, checked) \
      or loop(board, i, j-1, w+1, word, checked)

      checked.remove((i,j))
      return found

    # driver -> double for-loop, looking for starting indicies
    for i in range(self.max_i):
      for j in range(self.max_j):
        if board[i][j] == word[0]:
          found = loop(board, i, j, 0, word, set())
          if found:
            return True
    return False
  
  
# solved again
class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:

    self.max_i = len(board)
    self.max_j = len(board[0])

    target = word[0]

    def exists(board, word, visited, current, i, j, k) -> bool:
      if current == word:
        return True

      # handle all false cases
      if i < 0 or i >= self.max_i or j < 0 or j >= self.max_j or board[i][j] != word[k] or (i,j) in visited:
        return False

      tmp = current + board[i][j]

      visited.add((i,j))

      # terminate early, don't check if already found
      found = exists(board, word, visited, tmp, i-1, j, k+1) \
      or exists(board, word, visited, tmp, i+1, j, k+1) \
      or exists(board, word, visited, tmp, i, j-1, k+1) \
      or exists(board, word, visited, tmp, i, j+1, k+1)

      visited.remove((i,j))
      return found

    for i in range(self.max_i):
      for j in range(self.max_j):
        if board[i][j] == target and exists(board, word, set(), '', i, j, 0):
          return True
    return False

  
# solved yet again
# submitted and approved in one (1) attempt
class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
        
    def go(i: int, j: int, k: int, cur: str, seen):
      if cur == word:
        return True

      if (
        i < 0
        or i > len(board)-1
        or j < 0
        or j > len(board[0])-1
        or board[i][j] != word[k]
        or (i,j) in seen
      ):
        return False
            
      seen.add((i, j))
      k_ = k+1
      cur_ = cur+board[i][j]
            
      if any([
        go(i+1, j, k_, cur_, seen),
        go(i-1, j, k_, cur_, seen),
        go(i, j+1, k_, cur_, seen),
        go(i, j-1, k_, cur_, seen)
      ]):
        return True

      seen.remove((i, j))
            
            
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == word[0] and go(i,j,0,'',set()):
          return True
                
    return False
