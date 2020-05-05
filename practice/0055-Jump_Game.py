class Solution:
  def canJump(self, nums: List[int]) -> bool:
    # [3, 4, 0, 2, 4]
    # [4] is valid, target = 1
    # [2, 4] is valid because list.top = 2 and 2 > target = 0, target = 1
    # [0, 2, 4] is invalid because list.top = 0 and 0 < target = 1, target = 2
    # [4, 0, 2, 4] is valid because list.top = 4 and 4 > target = 2, target = 1
    # [3, 4, 0, 2, 4] is valid because list.top = 3 and 3 > target = 1, TRUE

    # [4, 2, 1, 0, 4]
    # [4] valid, target = 1, TRUE
    # [0, 4] invalid, target = 2, FALSE
    # [1, 0, 4] invalid, target = 3, FALSE
    # [2, 1, 0, 4] invalid, target = 4, FALSE
    # [4, 2, 1, 0, 4] valid, target = 1, TRUE

    r_nums = nums[::-1]
    current = [r_nums[0]]
    target = 1
    valid = True
    for num in r_nums[1:]:
      if num >= target:
        valid = True
        target = 1
      else:
        valid = False
        target += 1
    return valid
