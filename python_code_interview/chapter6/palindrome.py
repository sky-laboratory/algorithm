"""
chapter 1.
"""
import re
from collections import deque

input_str = "A man, a plan, a canal: Panama"


def solution(strs: str) -> bool:
    string_data = []
    
    for char in strs:
        if char.isalnum():
            string_data.append(char.lower())
    
    
    while len(string_data) > 1:
        if string_data.pop(0) != string_data.pop():
            return False
    
    return True


print(solution(input_str))