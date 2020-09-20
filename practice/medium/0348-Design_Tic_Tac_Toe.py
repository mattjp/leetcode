class TicTacToe:

  def __init__(self, n: int):
    """
    Initialize your data structure here.
    """
    self.board = [[0]*n for _ in range(n)]
    self.n = n
    self.diag1 = set()
    self.diag2 = set()
    for i in range(n):
      self.diag1.add((i,i))
      self.diag2.add((n-i-1, i))


  def check_win(self, l: List[int], player: int) -> bool:
    return all(map(lambda x: x==player, l))


  def move(self, row: int, col: int, player: int) -> int:
    """
    Player {player} makes a move at ({row}, {col}).
    @param row The row of the board.
    @param col The column of the board.
    @param player The player, can be either 1 or 2.
    @return The current winning condition, can be either:
            0: No one wins.
            1: Player 1 wins.
            2: Player 2 wins.
    """
    # moves are assumed to be valid
    self.board[row][col] = player
    r = self.board[row]
    if self.check_win(r, player):
      return player

    c = [self.board[i][col] for i in range(self.n)]
    if self.check_win(c, player):
      return player

    if (row,col) in self.diag1:
      d1 = []
      for i in self.diag1:
        u,v = i
        d1.append(self.board[u][v])
      if self.check_win(d1, player):
        return player

    if (row, col) in self.diag2:
      d2 = []
      for i in self.diag2:
        u,v = i
        d2.append(self.board[u][v])
      if self.check_win(d2, player):
        return player

    return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
