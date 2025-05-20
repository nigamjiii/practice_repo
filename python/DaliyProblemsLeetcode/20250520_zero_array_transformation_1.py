from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        diff_array = [0] * n

        for query in queries:
            l = query[0]
            r = query[1]
            diff_array[l] += 1

            if r + 1 < n:
                diff_array[r + 1] -= 1
        c_sum = 0
        for i in range(n):
            c_sum += diff_array[i]
            if c_sum < nums[i]:
                return False

        return True


link = 'https://leetcode.com/problems/zero-array-transformation-i/?envType=daily-question&envId=2025-05-20'