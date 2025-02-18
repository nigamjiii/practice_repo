from typing import List

# Brute force: O(m+n) T.C , O(m+n) S.C
class Solution:
    def mergeArray(self,nums1,nums2):
        m = len(nums1)
        n = len(nums2)
        res = [None]*(m+n)

        i = j = k = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            res[k] = nums1[i]
            i += 1
            k += 1
        
        while j < n:
            res[k] = nums2[j]
            j += 1
            k += 1

        return res
  
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = self.mergeArray(nums1,nums2)

        length = len(mergedArray)
        mid = (length + 1) // 2

        if length & 1 == 0:
            return (mergedArray[mid] + mergedArray[mid - 1]) / 2
        else:
            return mergedArray[mid - 1]


# Best force: O(log(min(m,n))) T.C , O(1) S.C      
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        tot = m + n
        half = tot // 2

        l = 0
        r = m - 1

        while True:
            mid = (l + r) // 2

            takenEle = mid + 1
            restEle = half - takenEle

            ALeft = nums1[mid] if (mid) >= 0 else float('-inf')
            ARight = nums1[mid + 1] if (mid + 1) <= (m-1) else float('inf')
            BLeft = nums2[restEle - 1] if (restEle - 1) >= 0 else float('-inf')
            BRight = nums2[restEle] if (restEle) <= (n-1) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if tot & 1 != 0:
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = mid - 1
            else:
                l = mid + 1
            


        
        
        