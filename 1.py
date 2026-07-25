#best first search

def Best_first_search(graph,start,goal,heuristic,path=[]):
    open = [(0,start)]
    closed = set()
    closed.add(start)

    while open:
        open.sort(key=lambda x: heuristic[x[1]],reverse=True)
        cost,node = open.pop()
        path.append(node)

        if node == goal:
            return cost,path
        
        closed.add(node)
        for neighbour,neighbour_cost in graph[node]:
            if neighbour not in closed:
                open.append((neighbour_cost+cost,neighbour))
                closed.add(neighbour)

    return

graph = {
    'A': [('B', 11), ('C', 14), ('D',7)],
    'B': [('A', 11), ('E', 15)],
    'C': [('A', 14), ('E', 8), ('D',18), ('F',10)],
    'D': [('A', 7), ('F', 25), ('C',18)],
    'E': [('B', 15), ('C', 8), ('H',9)],
    'F': [('G', 20), ('C', 10), ('D',25)],
    'G': [],
    'H': [('E',9), ('G',10)]
}

start = 'A'
goal = 'G'

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

result = Best_first_search(graph, start, goal, heuristic)

if result:
    print(f"Minimum cost path from {start} to {goal} is {result[1]}")
    print(f"Cost: {result[0]}")
else:
    print(f"No path from {start} to {goal}")

















def bfs(graph,start,goal,heuristic,path=[]):
    o = [(0,start)]
    c = set()
    c.add(start)

    while open:
        o.sort(key=lambda x: heuristic[x[1]],reverse=True)
        cost,n = o.pop()
        path.append(n)

        if n==goal:
            return c,path
        c.add(n)
        for nei,nei_c in graph[n]:
            if nei not in c:
                o.append(nei)
                c.add(nei)