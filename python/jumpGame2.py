from ast import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n == 1:
            return 0

        curr = 0
        max_reach = 0
        jump = 0

        for i in range(n-1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr:
                curr = max_reach
                jump += 1

            if curr >= n-1:
                break
        
        return jump
    
link = 'https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150'