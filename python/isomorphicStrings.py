from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(lambda: -1)
        t_map = defaultdict(lambda: -1)

        for i in range(len(s)):
            if s_map[s[i]] == -1 and t_map[t[i]] == -1:
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
                continue

            if s_map[s[i]] != t[i] or t_map[t[i]] != s[i]: 
                return False

        return True
        
link = 'https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150'