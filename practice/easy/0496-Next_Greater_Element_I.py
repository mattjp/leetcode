class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    from collections import defaultdict
    
    index = defaultdict(int)
    output = []
    for i,n in enumerate(nums2):
      index[n] = i
      
    for n in nums1:
      i = index[n]
      for j in range(i+1, len(nums2)):
        if nums2[j] > n:
          output.append(nums2[j])
          break
      else:
        output.append(-1)
        
    return output
