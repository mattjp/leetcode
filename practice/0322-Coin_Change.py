class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    # [1, 4, 5], 12 (3)
    # build optimal solution assuming we have only the first coin
    # rebuild optimal solutions using next coin - we know all amounts below new coin value are optimal

    # init
    # [0: 0, 1: _, 2: _, 3: _, 4: _, 5: _, 6: _, 7: _, 8: _, 9: _, 10: _, 11: _, 12: _]

    # 1
    # [0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12]

    # 4
    # [0: 0, 1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 4, 8: 2, 9: 3, 10: 4, 11: 5, 12: 3]

    # 5
    # [0: 0, 1: 1, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3]

    amounts = [float('inf')] * (amount + 1)
    amounts[0] = 0

    for coin in coins:
      for i in range(coin, amount + 1):
        amounts[i] = min(amounts[i], amounts[i - coin] + 1)
    return amounts[amount] if amounts[amount] != float('inf') else -1
