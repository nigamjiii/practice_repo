class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
    
link = 'https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150'