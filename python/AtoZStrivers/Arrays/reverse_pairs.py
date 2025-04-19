from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def merge_sort(arr, n):
            nonlocal count

            if n <= 1:
                return arr

            mid = n // 2

            left = merge_sort(arr[:mid], mid)
            right = merge_sort(arr[mid:], n - mid)

            i = j = 0
            while i < len(left):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
                i += 1

            left.extend(right)
            left.sort()
            return left

        merge_sort(nums, len(nums))
        return count


link = 'https://leetcode.com/problems/reverse-pairs/'