from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        n = len(nums)

        l = 0
        r = 0
        freq = {}
        count = 0

        while l <= r and r < n:
            if nums[r] in freq:
                freq[nums[r]] += 1
            else: 
                freq[nums[r]] = 1

            while len(freq) == k:
                count += (n - r)
                freq[nums[l]] -= 1

                if freq[nums[l]] == 0:
                    del freq[nums[l]]

                l += 1
                
            r += 1

        return count

link = 'https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24'