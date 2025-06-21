from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        nums.sort()

        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] <= k:
                ans.append(nums[i : i + 3])
            else:
                return []

        return ans

link = 'https://leetcode.com/problems/divide-array-into-arrays-of-max-difference-k/description/?envType=daily-question&envId=2025-06-18'