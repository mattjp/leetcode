class Solution:
  def numSquares(self, n: int) -> int:
    """
    do this like the coin change problem, but primes instead of coins
    """

    primes = []
    p = 1
    while p*p <= n:
      primes.append(p*p)
      p += 1

    nums = [0] * (n+1)

    for prime in primes:
      for i in range(prime, len(nums)):
        # we know `i - prime` gives us the optimal solution for the difference
        new_num = nums[i - prime] + 1
        # update optimal solution if we can get to `i` in fewer steps using the current prime
        if nums[i] == 0 or new_num < nums[i]:
          nums[i] = new_num

    return nums[-1]
