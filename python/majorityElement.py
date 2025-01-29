from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = defaultdict(lambda: 0)
        n = len(nums)
        
        for i in range(n):
            hash_map[nums[i]] += 1

        for key, value in hash_map.items():
            if value > n / 2:
                return key

link = 'https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150'