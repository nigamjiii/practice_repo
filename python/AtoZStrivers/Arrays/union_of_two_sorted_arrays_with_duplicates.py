class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        
        n = len(a)
        m = len(b)
        l,r = 0,0
        ans = []

        while l < n and r < m:
            if a[l] == b[r]:
                if len(ans) == 0 or ans[-1] != a[l]:
                    ans.append(a[l])
                l += 1
                r += 1
            elif a[l] < b[r]:
                if len(ans) == 0 or ans[-1] != a[l]:
                    ans.append(a[l])
                l += 1
            else:
                if len(ans) == 0 or ans[-1] != b[r]:
                    ans.append(b[r])
                r += 1
                
        while l < n:
            if len(ans) == 0 or ans[-1] != a[l]:
                ans.append(a[l])
            l += 1
            
        while r < m:
            if len(ans) == 0 or ans[-1] != b[r]:
                ans.append(b[r])
            r += 1
        
        return ans
    
    
link = 'https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays'