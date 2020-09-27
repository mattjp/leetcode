class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:      
      all_elems = set(range(1,len(nums)+1))
      nums_set = set(nums)
      return list(all_elems.difference(nums_set))
