class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = s.zfill(32)
        s = s[::-1]
        return int(s,2)
        
link = 'https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150'