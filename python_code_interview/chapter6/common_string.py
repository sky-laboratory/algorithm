import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def most_common_word(paragraph: str, banned: list[str]) -> str:
    words: list[str] = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]
    counts: list[tuple[str, int]] = Counter(words)
    return counts.most_common(1)[0][0]


print(most_common_word(paragraph, banned))
