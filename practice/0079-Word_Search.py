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
