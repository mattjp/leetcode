class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

    # Find the last occurance of the largest number in a `k` size window
    def get_new_max(sub_nums: List[int]):
      rev_sub_nums = sub_nums[::-1]
      index = rev_sub_nums.index(max(rev_sub_nums))
      return len(sub_nums) - index - 1

    # initialize everything
    l = 0
    r = k
    i = get_new_max(nums[l:r]) # largest number will always be stored as `i`
    l += 1
    r += 1    
    output = [nums[i]]

    # slide until end of array
    while r <= len(nums):
      # if the next number is largest, update `i`
      if nums[r-1] >= nums[i]:
        i = r-1
      # if `i` is no longer in the window, find the next largest
      elif l > i:
        i = l + get_new_max(nums[l:r])
      output.append(nums[i])
      l += 1
      r += 1

    return output
