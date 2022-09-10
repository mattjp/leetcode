class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sum([[n]*c for n,c in sorted(collections.Counter(nums).items(), key=lambda i: (i[1], -i[0]))], [])
      
