from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        if digits[n - 1] < 9:
            digits[n - 1] += 1
            return digits

        car = 1

        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                car = 0
                break
            digits[i] = 0

        if car:
            digits.insert(0, 1)

        return digits

link = 'https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150'