class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    """
    for each station i - 
    attempt to go around the entire array
    for each index, if the amount of gas we have now is less than we had when
    we previously attempted the index, break early
    """

    n = len(gas)
    attempted = {}
    
    for i in range(n):
      loc, cur_gas = i, gas[i]
      j = (loc+1) % n

      if loc in attempted and attempted[loc] <= cur_gas:
        continue
      else:
        attempted[loc] = cur_gas

      while cost[loc] <= cur_gas:
        if j == i:
          return i
        cur_gas -= cost[loc]
        cur_gas += gas[j]
        loc = (loc+1) % n
        j = (j+1) % n

    return -1
