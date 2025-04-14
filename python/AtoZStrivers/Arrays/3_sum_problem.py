from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for pivot in range(n - 2):
            # For skipping duplicates
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue

            l = pivot + 1
            r = n - 1
            target = -nums[pivot]

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.append([nums[pivot], nums[l], nums[r]])

                    # For skipping duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    # For skipping duplicates
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return ans
    
link = 'https://leetcode.com/problems/3sum/'
