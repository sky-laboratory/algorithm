nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# 브루투포스
def intersection(num1: list[int], num2: list[int]) -> list[int]:
    result: set = set()
    for data1 in num1:
        for data2 in num2:
            if data1 == data2:
                result.add(data1)
                
    return list(result)

from bisect import bisect_left
def intersection(num1: list[int], num2: list[int]) -> list[int]:
    result = set()
    num2.sort()
    for n1 in num1:
        i2: int = bisect_left(num2, n1)
        if len(num2) > 0 and len(num2) > i2 and n1 == num2[i2]:
            result.add(n1)

    return result


print(intersection(nums1, nums2))