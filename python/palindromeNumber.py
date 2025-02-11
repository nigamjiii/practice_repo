class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

# without using string conversion , T.C - O(log(n) base 10)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = x
        rev = 0

        while num > 0:
            rev = (rev * 10) + (num % 10)
            num //= 10

        return x == rev


link = 'https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150'