from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        k = 2

        count = 0

        while k < n:
            if nums[i] + nums[k] == nums[j] / 2:
                count += 1

            i += 1
            j += 1
            k += 1

        return count

link = 'https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/'