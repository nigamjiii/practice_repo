class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        ans = mapping[s[len(s) - 1]]

        for i in range(len(s) - 2, -1, -1):
            if mapping[s[i]] >= mapping[s[i+1]]:
                ans += mapping[s[i]]
            else:
                ans -= mapping[s[i]]

        return ans
    
link = 'https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150'