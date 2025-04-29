from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        maxi_count = nums.count(maxi)

        if maxi_count < k:
            return 0

        n = len(nums)
        i = 0
        j = 0
        count = 0
        curr_maxi_count = 0

        while j < n:
            if nums[j] == maxi:
                curr_maxi_count += 1

            if curr_maxi_count >= k:
                while i <= j and curr_maxi_count >= k:
                    count += (n - j)
                    if nums[i] == maxi:
                        curr_maxi_count -= 1
                    i += 1
            
            j += 1

        return count
                

link = 'https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29'