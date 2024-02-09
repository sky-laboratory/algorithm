input = "aasdfjasdcdcdcdbabad"
# Output: "bab"


def logest_palindromic(strs: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장 
    def expose(left: int, right: int) -> str:
        while left >= 0 and right < len(strs) and strs[left] == strs[right]:
            left -= 1
            right += 1
        return strs[left+1: right]

    if len(strs) < 2 or strs == strs[::-1]:
        return strs
    
    result = ""
    for i in range(len(strs)-1):
        result = max(
            result,
            expose(i, i+1),
            expose(i, i+2),
            key=len
        )
    return result


print(logest_palindromic(input))


