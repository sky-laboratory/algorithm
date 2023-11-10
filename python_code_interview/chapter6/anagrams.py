from collections import defaultdict

a = ["eat", "tea", "tan", "ate", "nat", "bat"]


def anagrams(a: list[str]) -> list[list[str]]:
    anergram = defaultdict(list)

    for ana_list in a:
        anergram["".join(sorted(ana_list))].append(ana_list)
    return list(anergram.values())


print(anagrams(a))
