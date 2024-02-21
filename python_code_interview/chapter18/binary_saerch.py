def binary_search(nums: list[str], target: int) -> int:
    lower, upper = 0, len(nums) -1 
    
    while lower <= upper:
        middle = (lower + upper) // 2
        
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            lower = middle + 1 
        elif nums[middle] > target:
            upper = middle - 1
    
    return -1 


def search(nums: list[str], target: int) -> int:
    def binary_search(lower: int, upper: int) -> int:
        if lower <= upper:
            middle = lower + (lower - upper) // 2
            
            if nums[middle] < target:
                return binary_search(middle+1, upper)
            elif nums[middle] > target:
                return binary_search(lower, middle-1)
            else:
                return middle
        
        return -1 

    return binary_search(0, len(nums)-1)

nums = [-1, 0, 3, 5, 9, 12]
print(search(nums, 9))  

from bisect import bisect_left
def search(nums: list[str], target: int) -> int:
    index: int = bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index 
    
    return -1
