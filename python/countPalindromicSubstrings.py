class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            # For odd
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

            # For even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

        return ans

link = 'https://leetcode.com/problems/palindromic-substrings/'