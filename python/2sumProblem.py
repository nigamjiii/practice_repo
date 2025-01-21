from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            temp = numbers[l] + numbers[r]
            if temp == target:
                break
            elif temp < target:
                l += 1
            else:
                r -= 1
        
        return [l+1, r+1]
        
link = 'https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150'