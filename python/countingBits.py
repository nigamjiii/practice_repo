from typing import List

# T.C - O(n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            n = i

            c = 0

            while n != 0:
                n = n & n - 1
                c += 1

            ans.append(c)

        return ans
    
# T.C -> O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1,n+1):
            ans[i] = ans[i//2] + (i & 1)
            
        return ans
        
        

link = 'https://leetcode.com/problems/counting-bits/description/'