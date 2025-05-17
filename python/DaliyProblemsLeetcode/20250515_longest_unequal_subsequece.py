from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        n = len(words)
        curr = -1

        for i in range(n):
            if curr == -1:
                curr = groups[i]
                ans.append(words[i])

            if curr != groups[i]:
                ans.append(words[i])
                curr = groups[i]

        return ans

link = 'https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/?envType=daily-question&envId=2025-05-15'