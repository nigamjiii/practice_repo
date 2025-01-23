from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1]

        for i in range(1,len(nums)):
            ans.append(ans[i-1]*nums[i-1])

        suffix = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * suffix
            suffix *= nums[i]

        return ans

link = 'https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150'