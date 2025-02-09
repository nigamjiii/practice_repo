class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
        
link = 'https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150'