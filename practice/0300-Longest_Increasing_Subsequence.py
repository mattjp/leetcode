class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    # assume previous sub array is optimally solved, only 
    # worry about adding new element

    # [3, 4, 7, 5, 6]
    # []
    # [3],             L = [3]
    # [3, 4],          L = [3, 4] <= 4 appended b/c 4 > 3
    # [3, 4, 7],       L = [3, 4, 7]
    # [3, 4, 7, 5],    L = [3, 4, 5] <= 5 replaces 7 b/c 5 < 7 & 5 > 4
    # [3, 4, 7, 5, 6], L = [3, 4, 5, 6]

    # [10, 9, 2, 5, 3, 7, 101, 18]
    # []
    # [10], L = [10]
    # [10, 9], L = [9] <= 9 replaces 10 b/c 9 < 10 & len=1
    # [10, 9, 2], L = [2]
    # [10, 9, 2, 5], L = [2, 5]
    # [10, 9, 2, 5, 3], L = [2, 3]
    # [10, 9, 2, 5, 3, 7], L = [2, 3, 7]
    # [10, 9, 2, 5, 3, 7, 101], L = [2, 3, 7, 101]
    # [10, 9, 2, 5, 3, 7, 101, 18], L = [2, 3, 7, 18]

    # [7, 8, 9, 1, 2, 3, 4]
    # 7, L = 7
    # 7, 8, L = 7, 8
    # 7, 8, 9, L = 7, 8, 9
    # 7, 8, 9, 1, L = 7, 8, 9 <= 1 not appended b/c 1 < 9 but 1 not > 8
    # 7, 8, 9, 1, 2, L = 7, 8, 9
    # 7, 8, 9, 1, 2, 3, L = 7, 8, 9
    # 7, 8, 9, 1, 2, 3, 4 L = 7, 8, 9

    res = 0
    for j in range(len(nums)):
      best = []
      for i in range(j, len(nums)):
        # for each i, we assume the previous array is perfectly solved
        if len(best) == 0:
          best.append(nums[i])
        elif nums[i] > best[-1]:
          best.append(nums[i])
        elif nums[i] < best[-1]:
          if len(best) == 1 or nums[i] > best[-2]:
            best.pop()
            best.append(nums[i])
      res = max(res, len(best))
    return res
