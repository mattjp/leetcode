class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    def search(nums: List[int], path: List[int]=[], cur: int=0):
      for i,num in enumerate(nums):
        if cur+num < target:
          search(nums[i:], path+[num], cur+num) # reduce search space so we don't look backwards
        else:
          if cur+num==target:
            self.output.append(path+[num])
          return # if input is sorted, we can just quit here
        
        
    self.output = []
    search(sorted(candidates))
    return self.output
