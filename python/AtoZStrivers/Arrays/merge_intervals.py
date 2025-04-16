from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if len(ans) != 0 and start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans

link = 'https://leetcode.com/problems/merge-intervals/'