from queue import Queue

graph: dict[int, list[int]] = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def iterative_bfs(start_v: int):
    discovered: list[int] = [start_v]
    
    queue = Queue()
    queue.put(start_v)
    while queue.empty() == False:
        v = queue.get()
        
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.put(w)
    
    return discovered
    

print(iterative_bfs(1))