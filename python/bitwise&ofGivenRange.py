# T.C - O(log n) S.C - O(1)
# Approach: Finding common prefix between left and right which will be same for our ans and adding all zeroes after that
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        c = 0

        while left != right:
            left >>= 1
            right >>= 1
            c += 1

        return left << c

        

            
link = 'https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=study-plan-v2&envId=top-interview-150'