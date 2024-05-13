def permute(nums: list[int]) -> list[list[int]]:
    results = []
    prev_elements = []
    
    def dfs(elements: list[int]) -> None:
        # 리프노드일때 추가 
        if len(elements) == 0:
            results.append(prev_elements[:])
    
        # 순열 재귀
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    
    dfs(nums)
    return results
print(permute([1, 2, 3]))

from itertools import permutations

def permute(num: list[int]) -> list[list[int]]:
    return list(map(list, permutations(num)))

print(permute([1, 2, 3]))