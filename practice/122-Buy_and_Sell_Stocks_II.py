class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit: int = 0
    curProfit: int = 0
    buyPrice = prices[0]
    for p in range(1, len(prices)):
      newProfit: int = prices[p] - buyPrice
      if newProfit < curProfit:
        profit += curProfit
        buyPrice = prices[p]
        curProfit = 0
      else:
        curProfit = newProfit
    profit += curProfit
    return profit
