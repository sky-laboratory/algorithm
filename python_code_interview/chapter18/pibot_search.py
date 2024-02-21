def pibot_search(nums: list[int], target: int) -> int:

    
    left, right = 0, len(nums) - 1
    while left < right:
        middle = left + (right - left) // 2 
        if nums[middle] > nums[right]:
            left = middle + 1 
        else:
            right = middle
    
    pivot = left
    left, right = 0, len(nums) - 1
    
    while left <= right:
        middle = left + (right - left) // 2 
        pivot_middle = (pivot + middle) % len(nums)
        
        if nums[pivot_middle] < target:
            left = middle - 1
        elif nums[pivot_middle] > target:
            right = middle + 1
        else:
            return middle

    return -1    

nums = [4, 5, 6, 7, 0, 1, 2]
print(pibot_search(nums, 1))