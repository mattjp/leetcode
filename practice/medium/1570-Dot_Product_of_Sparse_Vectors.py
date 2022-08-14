class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.vector[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i,v in vec.vector.items():
            if i in self.vector:
                res += (v * self.vector[i])

        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
