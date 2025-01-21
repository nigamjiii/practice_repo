from typing import List


def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0

        l = 0
        r = n - 1
        while l < r:
            temp = (r - l) * min(height[l], height[r])
            area = max(area,temp)

            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        
        return area

link = 'https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150'