from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        interesting_count = 0 # Counting valid nums till now
        rem_map = {0: 1} # Storing rem of total count till now if divide by modulo
        count = 0

        for num in nums:
            if (num % modulo) == k:
                interesting_count += 1

            r1 = interesting_count % modulo
            r2 = (r1 - k + modulo) % modulo

            if r2 in rem_map:
                count += rem_map[r2]

            if r1 in rem_map:
                rem_map[r1] += 1
            else:
                rem_map[r1] = 1

        return count
                

link = 'https://leetcode.com/problems/count-of-interesting-subarrays/?envType=daily-question&envId=2025-04-25'