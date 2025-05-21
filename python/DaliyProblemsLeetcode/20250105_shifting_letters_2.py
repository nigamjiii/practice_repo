from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        diff_arr = [0] * n
        l, r, val = -1, -1, -1

        for shift in shifts:
            l = shift[0]
            r = shift[1]
            val = shift[2]

            if val:
                diff_arr[l] += 1
                if r + 1 < n:
                    diff_arr[r + 1] -= 1
            else:
                diff_arr[l] -= 1
                if r + 1 < n:
                    diff_arr[r + 1] += 1

        prefix_sum = 0
        res = ""

        for i in range(n):
            prefix_sum += diff_arr[i]
            final_ascii = ord(s[i]) + prefix_sum
            wrapped_value = (final_ascii - 97) % 26 + 97  # Wrapping in lowercase range
            res += chr(wrapped_value)

        return res
    
link = 'https://leetcode.com/problems/shifting-letters-ii/?envType=daily-question&envId=2025-01-05'