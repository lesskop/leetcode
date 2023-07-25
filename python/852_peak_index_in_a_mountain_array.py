class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # # Linear
        # i = 0

        # while arr[i] < arr[i + 1]:
        #     i += 1
        
        # return i
    
        # Binary search
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        return left