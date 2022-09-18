class MyCalendar:
    """
    This passes, but would be faster if we used a sorted data structure.
    """

    def __init__(self):
        self.cal = []
        
        
    def overlap(self, start, end):
        for s, e in self.cal:
            if s < end and e > start:
                return True

        return False
    
    
    def addEvent(self, start, end):
        self.cal.append([start, end])
        i = len(self.cal)-1
        while i > 0 and self.cal[i][0] < self.cal[i-1][0]:
            self.cal[i], self.cal[i-1] = self.cal[i-1], self.cal[i]
        

    def book(self, start: int, end: int) -> bool:
        if self.overlap(start, end):
            return False
        self.addEvent(start, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
