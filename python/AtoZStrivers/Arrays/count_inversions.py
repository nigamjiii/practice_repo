def getInversions(arr, n):
    count = 0
    
    def merge_sort(array, n):
        nonlocal count
        if n == 1:
            return array

        mid = n // 2

        left = merge_sort(array[:mid], mid)
        right = merge_sort(array[mid:], n - mid)

        i = 0
        j = 0
        ans = []

        while i < mid and j < n - mid:
            if left[i] > right[j]:
                count += mid - i
                ans.append(right[j])
                j += 1
            else:
                ans.append(left[i])
                i += 1

        while i < mid:
            ans.append(left[i])
            i += 1

        while j < n - mid:
            ans.append(right[j])
            j += 1

        return ans

    merge_sort(arr, n)
    return count


link = 'https://www.naukri.com/code360/problems/count-inversions_615?leftPanelTabValue=PROBLEM'