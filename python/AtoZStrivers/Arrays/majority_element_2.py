from typing import List

# Better Solution, T.C= O(n) S.C = O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = {}
        ans = []

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        for key, val in hash_map.items():
            if val > (len(nums) // 3):
                ans.append(key)

        return ans
    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, el1 = 0, float('-inf')
        cnt2, el2 = 0, float('-inf')
        n = len(nums)
        ans = []

        for num in nums:
            if cnt1 == 0 and el2 != num:
                el1 = num
                cnt1 += 1
            elif cnt2 == 0 and el1 != num:
                el2 = num
                cnt2 += 1
            elif el1 == num:
                cnt1 += 1
            elif el2 == num:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1

        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ans.append(el1)
        if cnt2 >= mini:
            ans.append(el2)

        return ans
        
link = 'https://leetcode.com/problems/majority-element-ii/'
