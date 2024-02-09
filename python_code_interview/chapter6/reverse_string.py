input_data = ["h", "e", "l", "l", "o"]


def reverse_string(s: list[str]) -> list[str]:
    left, right = 0, len(s)-1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

reverse_string(input_data)