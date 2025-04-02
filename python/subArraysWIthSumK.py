from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_map = defaultdict(lambda: 0)
        prefix_sum_map[0] = 1 
        
        currSum = 0
        ans = 0
        for num in nums:
            currSum += num
            ans += prefix_sum_map[currSum - k]
            prefix_sum_map[currSum] += 1

        return ans

link = 'https://leetcode.com/problems/subarray-sum-equals-k/'