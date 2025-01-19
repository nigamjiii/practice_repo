class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1
        k = 1

        while i <= j and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[k] = nums[j]
                i = j
                j = i + 1
                k += 1
        
        return k
    
link = 'https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150'