class Solution:
  def change(self, amount: int, coins: List[int]) -> int:

  # there always exists 1 way to make 0 coins
  combinations = [1] + ([0] * amount)

  # for each coin, count the number of existing combinations
  for coin in coins:
    for c in range(coin, len(combinations)):
      # we know the difference is solved for optimally, so we add
      # the difference to the existing number of combinations
      d = c - coin
      combinations[c] += combinations[d]

  return combinations[amount]
