class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    cur_min = prices[0]
    cur_max = prices[0]
    global_max = 0

    for price in prices[1:]:
      # if this price is lower than the lowest price we've seen so far,
      # restart the search for a local max here
      if price < cur_min:
        cur_min = price
        cur_max = price
      # if this price is greater than the local max, update the local max
      elif price > cur_max:
        cur_max = price

      global_max = max(global_max, cur_max-cur_min)

    return global_max
