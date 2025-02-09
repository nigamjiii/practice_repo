from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            ans = ans ^ nums[i]

        return ans
        
link = 'https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150'