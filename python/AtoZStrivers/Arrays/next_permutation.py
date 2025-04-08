from typing import List

# Most optimal solution
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # first find index from where its not in increasing from back
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.sort()
            return

        tr = n - 1
        # find the just larger elemet from nums[i]
        while tr > i:
            if nums[tr] > nums[i]:
                nums[i], nums[tr] = nums[tr], nums[i] # swap
                break

            tr -= 1

        nums[i + 1 :] = nums[n - 1 : i : -1] # then reverse it


link = 'https://leetcode.com/problems/next-permutation/'