class Solution:
    def minPartitions(self, n: str) -> int:
        a = list(n)
        b = list(map(int, a))
        return max(b)
