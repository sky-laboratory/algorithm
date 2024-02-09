from collections import defaultdict

input = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrames = defaultdict(list)
    
    for word in strs:
        anagrames[''.join(sorted(word))].append(word)
    return list(anagrames.values())


group_anagrams(input)