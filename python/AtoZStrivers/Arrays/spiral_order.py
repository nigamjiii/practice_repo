from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        top, left = 0, 0
        bottom, right = m - 1, n - 1

        while top <= bottom and left <= right:
            # left -> right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1

            # top -> bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
                
            right -= 1
  
            if top <= bottom:
                # right -> left
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

                bottom -= 1

            if left <= right:
                # bottom -> top
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

                left += 1

        return ans

link = 'https://leetcode.com/problems/spiral-matrix/'