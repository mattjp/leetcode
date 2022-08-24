class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        """
        1. Create a whitelist from [n - len(blacklist), n]
        2. Iterate through blacklist, if i < min(whitelist) add deny_list entry
        3. When picking, select an int from 0 to min(whitelist)
            there are only [0, min(whitelist)] possibilities (b/c blacklist)
        """
        self.blacklist = {}
        self.search_space = n - len(blacklist)
        
        whitelist = set(range(self.search_space, n))
        
        for b in blacklist:
            if b in whitelist:
                whitelist.remove(b)
        
        for b in blacklist:
            if b < self.search_space:
                self.blacklist[b] = whitelist.pop()


    def pick(self) -> int:
        r = random.randint(0, self.search_space - 1)
        if r in self.blacklist:
            return self.blacklist[r]
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
