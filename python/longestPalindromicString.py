class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''

        for i in range(n):
            # For odd
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            # For even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res

        
link = 'https://leetcode.com/problems/longest-palindromic-substring/'