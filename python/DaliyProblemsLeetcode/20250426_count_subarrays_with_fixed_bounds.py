from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minKpos, maxKpos, culpritInd = -1, -1, -1
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                culpritInd = i

            if nums[i] == maxK:
                minKpos = i

            if nums[i] == minK:
                maxKpos = i
            
            smaller = min(minKpos, maxKpos)
            temp = smaller - culpritInd

            count += temp if temp > 0 else 0

        return count
        
link = 'https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26'