input_string = "A man, a plan, a canal: Panama"

# def is_parlindrome(strs: str) -> bool:
    
#     string_char = []
#     for data in strs:
#         if data.isalnum():
#             string_char.append(data.lower())
    
#     while 1 < len(string_char):
#         if string_char.pop(0) != string_char.pop():
#             return False
#     return True

# def is_parlindrome(strs: str) -> bool:
#     string_data = "".join(string.lower() for string in strs if string.isalnum()) 
#     return string_data == string_data[::-1]

# from collections import deque

# def is_parlindrome(s: str) -> bool:
#     strs: deque = deque()
    
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
    
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
    
#     return True

import re
def is_parlindrome(strs: str) -> bool:
    string_data = strs.lower()
    string_data = re.sub(r'[^a-z0-9]', '', string_data)
    return string_data == string_data[::-1]

print(is_parlindrome(input_string))