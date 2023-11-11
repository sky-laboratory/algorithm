import re
from collections import deque


def palindrome_deque(s: str) -> bool:
    # 자료형 데크로 선언
    strs: deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def palidrome_list(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def palidrome_slicing(s: str) -> bool:
    s = s.lower()
    # 정규 표현식 이용하기
    s: str = re.sub(r"[^a-z0-9]", "", s)

    return s == s[::-1]


input_str: str = "A man, a plan, a canal: Panama"
print(palidrome_slicing(input_str))
