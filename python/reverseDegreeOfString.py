class Solution:
    ascii_values = {chr(i): 123 - i for i in range(ord("a"), ord("z") + 1)}

    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            sum += Solution.ascii_values[s[i]] * (i + 1)

        return sum

link = 'https://leetcode.com/problems/reverse-degree-of-a-string/?slug=maximize-active-section-with-trade-i&region=global_v2'