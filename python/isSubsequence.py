class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        n = len(t)
        j = 0

        for i in range(n):
            if s[j] == t[i]:
                j += 1

            if j > len(s) - 1:
                return True

        return False
    
link = 'https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150'