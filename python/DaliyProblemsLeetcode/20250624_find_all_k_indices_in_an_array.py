from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        n = len(nums)
        diff_array = [0] * n

        for i in range(n):
            if nums[i] == key:
                diff_array[i - k if (i - k) >= 0 else 0] += 1
                if (i + k + 1) < n:
                    diff_array[i + k + 1] -= 1

        ans = []
        c_sum = 0

        for i in range(n):
            c_sum += diff_array[i]
            if c_sum:
                ans.append(i)

        return ans

link = 'https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/?envType=daily-question&envId=2025-06-24'