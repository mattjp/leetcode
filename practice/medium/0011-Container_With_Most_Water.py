# 11. Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

class Solution:
  def calcArea(self, h, w):
    return h*w

  def maxArea(self, height: List[int]) -> int:
    res, l, r = 0, 0, len(height)-1
    while l < r:
      res = max(res, self.calcArea(min(height[l], height[r]), r-l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    return res

# solved again
class Solution:
  def maxArea(self, height: List[int]) -> int: 
    max_area = 0
    l = 0
    r = len(height)-1

    while l < r:
      max_area = max(max_area, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    return max_area

  
