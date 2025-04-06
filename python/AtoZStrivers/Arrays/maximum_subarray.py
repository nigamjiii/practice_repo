from typing import List

# Optimal, T.C = O(n) S.C = O(1) 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        curr = 0

        for num in nums:
            curr += num
            if maxi < curr:
                maxi = curr
        
            if curr < 0:
                curr = 0
        
        return maxi
    
link = 'https://leetcode.com/problems/maximum-subarray/'