from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        if nums[r] < target:
            return r + 1

        if nums[l] > target:
            return l

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] > target:
                r = m - 1

            if nums[m] < target:
                l = m + 1

        return r + 1


link = 'https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150'