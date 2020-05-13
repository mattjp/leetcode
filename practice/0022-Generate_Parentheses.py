class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    # base case: opening and closing length are zero
    # while there are openings: add openings
    # when there are zero openings: add closings
    self.result = []

    def loop(opening: int, closing: int, current) -> None:
      if opening == closing == 0:
        self.result.append(current)
        return
      if opening > 0:
        loop(opening-1, closing, current+'(')
      if closing > 0 and closing > opening:
        loop(opening, closing-1, current+')')

    loop(n, n, '')
    return self.result
