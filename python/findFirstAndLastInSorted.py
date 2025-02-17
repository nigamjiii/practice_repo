from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1

        res = [-1, -1]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                if (
                    mid - 1 >= 0
                    and mid + 1 <= (n - 1)
                    and nums[mid - 1] == nums[mid]
                    and nums[mid + 1] != nums[mid]
                ):
                    res[1] = mid
                    r = mid - 1
                elif (
                    mid - 1 >= 0
                    and mid + 1 <= (n - 1)
                    and nums[mid + 1] == nums[mid]
                    and nums[mid - 1] != nums[mid]
                ):
                    res[0] = mid
                    l = mid + 1
                else:
                    l = mid - 1
                    r = mid + 1

                    while l >= 0 and nums[l] == target:
                        l -= 1
                    res[0] = l + 1

                    while r <= (n - 1) and nums[r] == target:
                        r += 1
                    res[1] = r - 1

                    return res

        return res


link = 'https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150'