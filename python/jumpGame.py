from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        targetIndex = n - 1

        for i in range(n - 2, -1, -1):
            if nums[i] >= targetIndex - i:
                targetIndex = i
            else:
                continue

            if targetIndex == 0:
                return True
        
        return False
    
link = 'https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150'