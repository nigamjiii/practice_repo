from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, m = 0, 0
        n = len(nums)
        r = n - 1

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1

link = 'https://leetcode.com/problems/sort-colors/'
        
        
        