from typing import *


# Memoization
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for _ in range(3)] for _ in range(n)]

    def rec(day, prev_task_ind): 
        # base case
        if dp[day][prev_task_ind] != -1:
            return dp[day][prev_task_ind]

        if day == 0:
            maxi = float('-inf')

            for i in range(3):
                if i != prev_task_ind:
                    maxi = max(maxi, points[0][i])

            dp[day][prev_task_ind] = maxi
            return dp[day][prev_task_ind]

        maxi = 0
        for i in range(3):
            if i != prev_task_ind:
                curr = points[day][i] + rec(day - 1, i)
                maxi = max(curr,maxi)

        dp[day][prev_task_ind] = maxi
        return dp[day][prev_task_ind]

    return rec(n-1,-1)

link = 'http://naukri.com/code360/problems/ninja-s-training_3621003?leftPanelTabValue=PROBLEM'


