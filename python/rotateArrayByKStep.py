class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[-k:] + nums[:-k]

link = 'https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150'