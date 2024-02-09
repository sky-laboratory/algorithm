import re
from collections import Counter

input_data = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# output
"ball"

def most_common_word(strs: str, banned: list[str]) -> str:
    words = [data for data in re.sub(r"[^\w]", " ", strs).lower().split() if data not in banned]
    return Counter(words).most_common(1)[0][0]


print(most_common_word(input_data, banned))

