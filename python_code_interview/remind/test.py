def logest_palindrome(strs: str) -> bool:
    def expose(left: int, right: int) -> str:
        while left >= 0 and len(strs) > right and strs[left] == strs[right]:
            left -=1
            right += 1
        
        return str[left+1: right]
    
    if len(strs) < 2 or strs[::-1]:
        return True
    
    result = ""
    for i in range(len(strs)-1):
        result = max(
            result,
            expose(i, i+1),
            expose(i, i+2),
            key=len
        )
    return result

input = "aasdfjasdcdcdcdbabad"
print(logest_palindrome(input))
