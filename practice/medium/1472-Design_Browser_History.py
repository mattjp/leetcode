class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.pointer = 0
        

    def visit(self, url: str) -> None:
        # remove all forward history
        self.pages = self.pages[:self.pointer + 1]
        # append and set pointer
        self.pages.append(url)
        self.pointer = len(self.pages) - 1
        

    def back(self, steps: int) -> str:
        self.pointer -= steps
        if self.pointer < 0:
            self.pointer = 0
        return self.pages[self.pointer]
        

    def forward(self, steps: int) -> str:
        self.pointer += steps
        if self.pointer >= len(self.pages):
            self.pointer = len(self.pages) - 1
        return self.pages[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
