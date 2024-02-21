numbers = [2, 7, 11, 15]
target = 9


from bisect import bisect_left
def two_sum(numbers: list[int], target: int) -> list[int]:
    for index, value in enumerate(numbers):
        expected = target - value
        i = bisect_left(numbers, expected, index+1)
        if i < len(numbers) and numbers[i] == expected:
            return index+1, i+1
        

print(two_sum(numbers, target))


def two_sum(numbers: list[int], target: int) -> list[int]:
    left, rigth = 0, len(numbers) - 1 
    
    while not left == rigth:
        if numbers[left] + numbers[rigth] < target:
            left += 1
        elif numbers[left] + numbers[rigth] > target:
            rigth -= 1
        else:
            return left+1, rigth+1
    return -1

def two_sum(numbers: list[int], target: int) -> list[int]:
    for index, value in enumerate(numbers):
        left, right = index+1, len(numbers)-1
        expected = target - value
        
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1 
            else:
                return index+1, mid+1
                
    return -1

