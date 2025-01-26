class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.strip().split()

        s_arr[:] = s_arr[::-1]

        return ' '.join(s_arr)
    
link = 'https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150'