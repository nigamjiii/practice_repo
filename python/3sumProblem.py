class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1

            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if s==0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while(l < r and nums[l] == nums[l-1]):
                        l += 1
                    while(l < r and nums[r] == nums[r+1]):
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res
    
link = 'https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150'