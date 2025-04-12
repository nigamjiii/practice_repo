from typing import List


class Solution:
    def nCr(self, n, r):
        if n == 0 or r == 0:
            return 1

        ans = 1

        for i in range(r):
            ans = (ans * (n - i)) // (i + 1)

        return ans

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            curr = []

            for j in range(i + 1):
                curr.append(self.nCr(i, j))

            ans.append(curr)

        return ans
    
link = 'https://leetcode.com/problems/pascals-triangle/'
