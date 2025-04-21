from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        curr_prefix = 0

        for diff in differences:
            curr_prefix += diff
            min_val = min(min_val, curr_prefix)
            max_val = max(max_val, curr_prefix)

        req_range = max_val - min_val
        given_range = upper - lower + 1

        if req_range > given_range:
            return 0

        return given_range - req_range


link = 'https://leetcode.com/problems/count-the-hidden-sequences/?envType=daily-question&envId=2025-04-21'