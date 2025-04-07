from typing import List

# Optimal Solution, only applies if positive and negative both are same otherwise create two array for storing positive and negative
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        ans = [None] * len(nums)

        for num in nums:
            if num & 1 << 31 != 0:
                ans[neg] = num
                neg += 2
            else:
                ans[pos] = num
                pos += 2

        return ans
    
link = 'https://leetcode.com/problems/rearrange-array-elements-by-sign/'
    

