class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        """
        For each num in nums, map num to the other values that form a perfect square
        We also need to keep track of the count of each value to handle duplicates
        
        [1, 17, 8]
        (1: 1, 17: 1, 8: 1)
        
        {
            1:  [8],
            8:  [1, 17],
            17: [8]
        }
        
        [2, 2, 2, 7]
        (2: 3, 7: 1)
        
        {
            2: [2, 7],
            7: [2]
        }
        
        If there exists a num that has no entries in the map, the problem has no solution
        
        For each key in the map, perform DFS
        Even if a key has multiple entries, we only need to DFS 1 time per entry
        If the DFS can reach every node, that search is a solution
        
        In the end, we use a global count of the used variables `available`
        """
        
        
        def isSquare(x, y):
            sqrt = (x + y) ** 0.5
            return sqrt == int(sqrt)
        
        
        def findPerfectSquares(nums):
            squares = {}
            
            for i,x in enumerate(nums):
                if x in squares:
                    continue
                squares[x] = set()
                for j,y in enumerate(nums):
                    if i != j and isSquare(x, y):
                        squares[x].add(y)

            return squares
        
        
        def validate(nums, squares):
            for num in nums:
                if num not in squares or len(squares[num]) < 1:
                    return False
            return True
        
        
        def dfs(num, perm, squares):
            if len(perm) == len(nums):  # If lengths are equal, we've added all elements
                cache.add(''.join([str(p) for p in perm]))
                return
            
            for sq in squares[num]:
                available[num] -= 1  # Subtract 1 from the parent count
                if available[sq] > 0:
                    dfs(sq, perm+[sq], squares)
                available[num] += 1

        
        # Get all the possible squares. These will be the nodes in the graph.
        squares = findPerfectSquares(nums)
        
        # If there exists a num with no squares, the problem is impossible.
        if not validate(nums, squares):
            return 0
        
        available = collections.Counter(nums)
        cache = set()
        
        # Perform DFS trying each num as the starting node.
        for num in nums:
            dfs(num, [num], squares)

        # Return all unique permutations
        return len(cache)
