class Solution:
    def cal(self, x, n):
        ans = 1
        t = x
        while n != 0:
            if n & 1 == 0:
                t = t * t
                n = n // 2
            else:
                ans *= t
                n = n - 1

        return ans

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.cal(x, abs(n))

        return self.cal(x, n)


       
        
link = 'https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150'