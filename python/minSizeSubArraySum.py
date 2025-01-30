from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        length = float('inf')

        if n == 1:
            return 1 if nums[0] >= target else 0

        l = 0
        s = 0

        for r in range(n):
            s += nums[r]

            while s >= target:
                length = min(length, r - l + 1)
                s -= nums[l]
                l += 1

        

        return length if length != float('inf')  else 0
    
link = 'https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150'

            
            

        
        