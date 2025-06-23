class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def superpalindromesInRange(self, left: str, right: str) -> int:
        count = 0
        left, right = int(left), int(right)

        for num in range(1, 100000):
            st = str(num)
            odd = st + st[-2::-1]
            even = st + st[::-1]

            sq_odd = int(odd) ** 2
            if sq_odd > right:
                break

            if sq_odd >= left and self.isPalindrome(str(sq_odd)):
                count += 1

            sq_even = int(even) ** 2

            if sq_even >= left and sq_even <= right and self.isPalindrome(str(sq_even)):
                count += 1

        return count

link = 'https://leetcode.com/problems/super-palindromes/'