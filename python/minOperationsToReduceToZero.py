from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        totSum = sum(nums)
        targetSum = totSum - x
        n = len(nums)

        if targetSum == 0:
            return n

        if targetSum < 0:
            return -1

        left = 0
        currSum = 0
        maxLen = float("-inf")

        for right in range(n):
            currSum += nums[right]

            while left <= right and currSum > targetSum:
                currSum -= nums[left]
                left += 1

            if currSum == targetSum:
                maxLen = max(right - left + 1, maxLen)

        return (n - maxLen) if maxLen != float("-inf") else -1


link = 'https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/'