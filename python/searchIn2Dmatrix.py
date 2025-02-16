from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        r_min = 0
        r_max = m - 1

        while(r_min<=r_max):
            r_mid = (r_min + r_max) // 2

            c_min = 0
            c_max = n - 1

            while(c_min<=c_max):
                c_mid = (c_min + c_max) // 2

                if matrix[r_mid][c_mid] == target:
                    return True

                if matrix[r_mid][c_mid] > target:
                    c_max = c_mid - 1

                if matrix[r_mid][c_mid] < target:
                    c_min = c_mid + 1
            
            if matrix[r_mid][0] > target:
                r_max = r_mid - 1

            if matrix[r_mid][0] < target:
                r_min = r_mid + 1
        

        return False
    
link = 'https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150'