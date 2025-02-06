class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()

        if len(pattern) != len(s_arr):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s_arr)):
            if s_arr[i] not in s_map and pattern[i] not in t_map:
                s_map[s_arr[i]] = pattern[i]
                t_map[pattern[i]] = s_arr[i]
            elif s_map.get(s_arr[i]) != pattern[i] or t_map.get(pattern[i]) != s_arr[i]:
                return False

        return True
    
link = 'https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150'