from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        my_set = set(nums)
        ans = 1

        for num in my_set:
            # find the smallest no. from where a sequence can start
            if num - 1 not in my_set: 
                c = 0
                curr = num

                while curr in my_set:
                    c += 1
                    curr += 1

                ans = max(ans, c)

        return ans


link = 'https://leetcode.com/problems/longest-consecutive-sequence/description/'