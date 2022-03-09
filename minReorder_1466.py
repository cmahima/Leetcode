def minReorder( n: int, connections) -> int:
    neighbors = {city: [] for city in range(n)}
    changes = 0
    visit = set()
    edges = {(a,b) for a,b in connections}

    for a,b in connections:
        neighbors[a].append(b)
        neighbors[b].append(a)

    def dfs(city):
        nonlocal neighbors, changes, visit, edges

        for neighbor in neighbors[city]:
            if neighbor in visit:
                continue
            if (neighbor,city) not in edges:
                changes +=1
            visit.add(neighbor)
            dfs(neighbor)
    visit.add(0)
    dfs(0)

    return changes

print(minReorder(n = 3, connections = [[1,0],[2,0]]))