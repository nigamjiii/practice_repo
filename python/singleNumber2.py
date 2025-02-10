from typing import List

link = 'https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150'


# naive approach : T.C = O(n*n) S.C = O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        look_up_set = set()
        for num in nums:
            if num not in look_up_set:
                count = nums.count(num)
                if count == 1:
                    return num
                look_up_set.add(num)


# better approach : T.C = O(n) S.C = O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f_map = {}
        for num in nums:
            if num not in f_map:
                f_map[num] = 1
                continue
            f_map[num] += 1

        for key, val in f_map.items():
            if val == 1:
                return key

# expected approach : T.C = O(n) S.C = O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)

        return ones

