class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.l = [None] * n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        output = []
        while self.ptr < len(self.l) and self.l[self.ptr] != None:
            output.append(self.l[self.ptr])
            self.ptr += 1
        return output
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
