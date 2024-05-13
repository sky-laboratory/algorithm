a = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5

def target_in_metrix(metrix: list[list[int]], target: int) -> bool:
    return any(target in data for data in metrix)

print(target_in_metrix(a, target))