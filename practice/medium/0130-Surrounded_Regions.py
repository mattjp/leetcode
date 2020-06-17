class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    # 1. DFS from exterior, change all Os to Zs
    # 2. Turn all remaining Os to Xs
    # 3. Turn all Zs to Os

    if len(board) == 0 or len(board[0]) == 0:
      return

    self.max_i = len(board)
    self.max_j = len(board[0])

    # flip board[i][j] to 'Z' then DFS
    def flipz(i, j):
      if i >= 0 and i < self.max_i and j >= 0 and j < self.max_j and board[i][j] == 'O':
        board[i][j] = 'Z'
        flipz(i-1, j)
        flipz(i+1, j)
        flipz(i, j-1)
        flipz(i, j+1)


    # search top and bottom row
    for j in range(self.max_j):
      if board[0][j] == 'O':
        flipz(0, j)
      if board[self.max_i-1][j] == 'O':
        flipz(self.max_i-1, j)

    # search first and last column
    for i in range(self.max_i):
      if board[i][0] == 'O':
        flipz(i, 0)
      if board[i][self.max_j-1] == 'O':
        flipz(i, self.max_j-1)

    # flip remaining Os to Xs and Zs to Os
    for i in range(self.max_i):
      for j in range(self.max_j):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        if board[i][j] == 'Z':
          board[i][j] = 'O'
