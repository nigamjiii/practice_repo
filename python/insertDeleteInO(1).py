import random


class RandomizedSet:

    def __init__(self):
        self.s = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.s)
        self.s.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last = self.s[-1]
            to_rem = self.s[self.dict[val]]

            self.s[self.dict[val]] = last
            self.dict[last] = self.dict[val]
            self.s[-1] = to_rem

            self.s.pop()
            self.dict.pop(val)
            return True
        
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.s)
        

link = 'https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150'