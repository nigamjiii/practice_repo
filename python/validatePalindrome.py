import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(new_str) - 1

        while l <= r:
            if(new_str[l] != new_str[r]):
                return False
            else:
                l += 1
                r -= 1
        
        return True
    
link = 'https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150'