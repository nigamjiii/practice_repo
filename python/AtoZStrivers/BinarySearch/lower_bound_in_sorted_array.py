def lowerBound(arr: [int], n: int, x: int) -> int: # type: ignore
    l = 0
    r = n - 1
    ans = n

    while l <= r:
        mid = (l+r) // 2

        if arr[mid] >= x:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return ans
            
    
link = 'https://www.naukri.com/code360/problems/lower-bound_8165382?leftPanelTabValue=PROBLEM'