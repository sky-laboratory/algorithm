graph: dict[int, list[int]] = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def recursive_dfs(element: int, target: dict[int, list[int]], discovered: list = []) -> list[int]:
    discovered.append(element)
    for data in target[element]:
        if data not in discovered:
            discovered = recursive_dfs(data, target)
    return discovered
    

def recursive_iterator(start_v: int, target: dict[int, list[int]]) -> list[int]:
    stack: list = [start_v]
    discovered: list[int] = []
    
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for data in target[v]:
                stack.append(data)
    
    return discovered


print(recursive_iterator(1, graph))