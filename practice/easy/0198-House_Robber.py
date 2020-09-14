class Solution:
  def rob(self, nums: List[int]) -> int:
    """
    dynamic programming
    keep track of the best haul at each house
    calculated haul for a given house is the max of
    stealing from this house + optimal solution 2 houses ago
    or the optimal solution of stealing from 1 house ago
    """
    if len(nums) < 1:
      return 0
    
    haul = [0, nums[0]]
    
    for i in range(1, len(nums)):
      haul.append(max(nums[i] + haul[-2], haul[-1]))
    return haul[-1]
