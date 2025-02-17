from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        ans = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if (
                nums[l] <= nums[mid]
            ):  # Check equality for boundary condition if mid and l points same element
                ans = min(nums[l], ans)
                l = mid + 1
            else:
                ans = min(nums[mid], ans)
                r = mid - 1

        return ans

link = 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150'