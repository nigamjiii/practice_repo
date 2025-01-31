from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)
        all_zero = True
        for i in range(n):
            if citations[i]:
                all_zero = False

        if all_zero:
            return 0
        
        mx = 1

        for i in range(n):
            if (n - 1 - i) >= citations[i] - 1:
                mx = max(mx, citations[i])
            else:
                mx = max(mx, n - i)

        return mx

link = 'https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150'