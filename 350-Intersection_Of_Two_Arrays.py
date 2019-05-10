# 350. Intersection of Two Arrays
# 
# Given two arrays, write a function to compute their intersection.

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    d = {}
    for num in nums1:
      if num not in d:
        d[num] = 0
      d[num] += 1
    r = []
    for num in nums2:
      if num in d:
        if d[num] > 0:
          r.append(num)
          d[num] -= 1
    return r
