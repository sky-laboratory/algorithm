nums = [2, 7, 11, 15]
target = 9


# 브루트포스 
def two_sum_numbering(number: list[int], target: str) -> list[int]:
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in 을 이용한 탐색 
def two_sum_numbering_in(number: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement: int = target - n 
        if complement in number[i + 1:]:
            return [number.index(n), number[i + 1:].index(complement) + (i + 1)]


# 첫 번째 수를 뺸 결과 키 조회 
def two_sum_numbering_first(number: list[int], target: int) -> list[int]:
    nums_map: dict[int, int] = {}
    for i, num in enumerate(number):
        nums_map[num] = i
        
    for i, num in enumerate(number):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

        

print(two_sum_numbering_first(nums, target))