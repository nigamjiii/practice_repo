class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:]=nums1[:m]
        nums2[:]=nums2[:n]

        nums1.extend(nums2)
        nums1.sort()

link = 'https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150'