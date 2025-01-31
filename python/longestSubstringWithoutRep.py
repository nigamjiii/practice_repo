class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        n = len(s)

        if n == 0:
            return 0
        
        l = 0
        mx_len = 1

        for r in range(n):
            while s[r] in char_set:  
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            if (r - l + 1) > mx_len:
                mx_len = r - l + 1

        return mx_len
                


link = 'https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150'