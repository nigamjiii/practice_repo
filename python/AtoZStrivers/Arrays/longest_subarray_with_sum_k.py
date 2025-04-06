class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        prefix_sum = 0
        sum_map = {}
        ans = 0
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                ans = i + 1
            elif (prefix_sum - k) in sum_map:
                ans = max(ans, i + 1 - sum_map[prefix_sum - k])
                
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i + 1
                
        
        return ans
        
link = 'https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k'