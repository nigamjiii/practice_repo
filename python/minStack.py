class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append((val,self.min))

    def pop(self) -> None:
        self.stack.pop()

        if len(self.stack) == 0:
            self.min = float('inf')
        else:
            self.min = self.stack[-1][1]
      
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
link = 'https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150'