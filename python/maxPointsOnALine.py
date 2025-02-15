from ast import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n - 1):
            hash_map = {}
            for j in range(i + 1, n):
                m = (
                    (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    if points[j][0] != points[i][0]
                    else "None"
                )

                if m not in hash_map:
                    hash_map[m] = 1
                else:
                    hash_map[m] += 1

            m_max = max(hash_map.values())
            if (m_max + 1) > ans:
                ans = m_max + 1

        return ans

link  = 'https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150'