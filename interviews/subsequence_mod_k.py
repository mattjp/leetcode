# Return number of subsequences that are divisible by k

def Solution(self, nums, k):
  r = 0
  curSum = 0
  modSums = {}
  modSums[0] = 1

  for i in range(len(nums)):
    curSum += nums[i]
    x = curSum % k
    x = k-x if x != 0 else 0
    if x in modSums:
      r += modSums[x]
    if x not in modSums:
      modSums[x] = 1
    else:
      modSums[x] += 1
  return r
