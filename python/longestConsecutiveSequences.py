from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hash_set = set(nums)
        max_len = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                length = 1
                while num + length in hash_set:
                    length += 1
                max_len = max(max_len, length)

        return max_len

link = 'https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150'