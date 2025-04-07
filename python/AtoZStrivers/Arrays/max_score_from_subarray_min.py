class Solution:
    def pairWithMaxSum(self, arr):
        n  = len(arr)
        l = 0
        r = l + 1
        
        ans = float('-inf')
        curr = 0
        
        while r < n:
            curr = arr[l] + arr[r]
            
            if ans < curr:
                ans = curr
            
            l += 1
            r += 1
        
        return ans
    
link = 'https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays'