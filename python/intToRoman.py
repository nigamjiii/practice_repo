class Solution:
    def intToRoman(self, num: int) -> str:
        dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''

        for i in range(len(dec)):
            res += rom[i] * (num // dec[i])
            num %= dec[i]

        return res
    
link = 'https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150'