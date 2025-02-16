from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            if (m - 1 >= 0 and nums[m] > nums[m-1] and m + 1 < n and nums[m] > nums[m+1]) or (m - 1 < 0 and nums[m] > nums[m+1]) or (m + 1 > n - 1 and nums[m] > nums[m-1]):
                return m

            if m - 1 >= 0 and nums[m] < nums[m-1]:
                r = m - 1
            elif m + 1 < n and nums[m] < nums[m+1]:
                l = m + 1

            
        return -1

link = 'https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150'