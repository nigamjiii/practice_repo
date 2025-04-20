class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low >= high:
            return
        
        partitionIndex = self.partition(arr, low, high)
        
        self.quickSort(arr, low, partitionIndex - 1)
        self.quickSort(arr, partitionIndex + 1, high)
        
    
    def partition(self,arr,low,high):
        
        pivot = low # decide pivot
        
        i = low
        j = high
        
        # find partition
        while i < j:
            while i <= high and arr[i] <= arr[pivot]:
                i += 1
                
            while j >= low and arr[j] > arr[pivot]:
                j -= 1
                
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                
        
        # place pivot in it's correct position
        if j != pivot:
            arr[j], arr[pivot] = arr[pivot], arr[j]
        
        return j
