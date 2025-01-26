from typing import List

# Better Approach (O(n*m)) => Good if n is small
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        m = 999
        for i in range(len(strs)):
            m = min(m, len(strs[i]))

        res = ''

        for j in range(m):
            is_present = True
            for i in range(1, len(strs)):
                if strs[i][j] != pivot[j]:
                    is_present = False
                    return res
            
            if is_present:
                res += pivot[j]
        
        return res
    
# optimal approach (O(n*log(n) + m)) => Good if n is large
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        res = ''
        n = len(strs)

        l = min(len(strs[0]), len(strs[n-1]))

        for i in range(l):
            if strs[0][i] != strs[n-1][i]:
                return res
            res += strs[0][i]

        return res
    
link = 'https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150'
