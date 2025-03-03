from typing import List


# Brute-Force: T.C -> O(n) and S.C -> O(2n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix_max = [float("-inf")] * (n + 1)
        suffix_max = [float("-inf")] * (n + 1)

        for i in range(n):
            prefix_max[i + 1] = max(prefix_max[i + 1], height[i], prefix_max[i])
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i], suffix_max[i])

        tot = 0
        for i in range(n):
            if prefix_max[i + 1] > height[i] and suffix_max[i] > height[i]:
                tot += min(prefix_max[i + 1], suffix_max[i]) - height[i]

        return tot

# Better Approach: T.C -> O(n) and S.C -> O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = float("-inf")
        suffix_max = [float("-inf")] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i], suffix_max[i])

        tot = 0
        for i in range(n):
            if height[i] > left_max:
                left_max = height[i]

            if left_max > height[i] and suffix_max[i] > height[i]:
                tot += min(left_max, suffix_max[i]) - height[i]

        return tot

# Best Approach: T.C -> O(n) and S.C -> O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = right_max = 0

        l = 0
        r = n - 1
        res = 0

        while l <= r:
            if height[l] < height[r]:
                if height[l] < left_max:
                    res += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if height[r] < right_max:
                    res += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1

        return res

