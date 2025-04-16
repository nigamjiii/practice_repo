from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # boundary check
        if n < 4:
            return []

        ans = []
        nums.sort()

        for first in range(n - 3):

            if first != 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, n - 2):

                if second != first + 1 and nums[second] == nums[second - 1]:
                    continue

                tar = target - nums[first] - nums[second]
                third = second + 1
                fourth = n - 1

                while third < fourth:
                    temp = nums[third] + nums[fourth]

                    if temp < tar:

                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1

                        third += 1
                    elif temp > tar:
                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1
                        fourth -= 1
                    else:
                        ans.append(
                            [nums[first], nums[second], nums[third], nums[fourth]]
                        )
                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1

                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1

                        third += 1
                        fourth -= 1

        return ans

link = 'https://leetcode.com/problems/4sum/'