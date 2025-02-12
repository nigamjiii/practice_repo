class Solution:
    def countOfNumbers(self, n, k):
        co = 0
        ni = k
        while k <= n:
            co += n // k
            k *= ni
        return co

    def trailingZeroes(self, n: int) -> int:
        return min(self.countOfNumbers(n, 2), self.countOfNumbers(n, 5))
    
link = 'https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150'