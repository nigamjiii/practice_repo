class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split()
        n = len(arr)

        return len(arr[n-1])
    
link = 'https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150'