from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l = 0
        r = n - 1

        while l<=r:
            m = (l+r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


link = 'https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150'