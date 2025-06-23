class Solution:
    decimal_palindromes = {}

    @classmethod
    def generateAllDecimalPalindromes(cls, length):
        if length == 0:
            return

        if length in cls.decimal_palindromes:
            return

        L = (length + 1) // 2
        min_num = pow(10, L - 1)
        max_num = pow(10, L) - 1

        res = []

        for num in range(min_num, max_num + 1):
            st = str(num)
            rev_st = st[::-1]

            if length & 1 == 0:
                res.append((st + rev_st))
            else:
                res.append((st + rev_st[1:]))

        cls.decimal_palindromes[length] = res

    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def generateBaseKString(self, num, k):
        res = ""

        while num > 0:
            res += str(num % k)
            num = num // k

        return res[::-1]

    def kMirror(self, k: int, n: int) -> int:
        tot = 0
        length = 1
        count = 0

        while count < n:
            Solution.generateAllDecimalPalindromes(length)

            l_length_decimal_palindromes = Solution.decimal_palindromes[length]

            for pal in l_length_decimal_palindromes:
                base_k_str = self.generateBaseKString(int(pal), k)

                if self.isPalindrome(base_k_str):
                    count += 1
                    tot += int(pal)

                    if count == n:
                        break

            length += 1

        return tot

link = 'https://leetcode.com/problems/sum-of-k-mirror-numbers/description/?envType=daily-question&envId=2025-06-23'