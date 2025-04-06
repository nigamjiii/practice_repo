from typing import List

# Optimal solution , T.C = O(n) , S.C = O(1) , This is Moore's Voting Algo
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        el = 0

        for num in nums:
            if c == 0:
                c += 1
                el = num
            elif num == el:
                c += 1
            else:
                c -= 1

        return el
        
link = 'https://leetcode.com/problems/majority-element/'