class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        m = 1

        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                m += 1
            else:
                m = 1

            if m <= 2:
                nums[k] = nums[j]
                k += 1

        return k

link = 'https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150'