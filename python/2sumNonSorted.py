from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]

            hash_map[nums[i]] = i


link = 'https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150'