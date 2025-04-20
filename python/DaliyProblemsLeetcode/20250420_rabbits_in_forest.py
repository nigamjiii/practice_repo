from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0

        answers.sort()
        i = 0
        n = len(answers)

        while i < n:
            ans += (answers[i] + 1)
            j = 1

            while i + j < n and j <= answers[i]:
                if answers[i] == answers[i+j]:
                    j += 1
                else:
                    break

            i += j

        return ans
    
link = 'https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20'