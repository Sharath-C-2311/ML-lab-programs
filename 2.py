h={
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}


# def Astar(start,stop):
    
#     open = set(start)
#     close = set()
#     g = {}
#     parent={}
#     g[start] = 0
#     parent[start] = start

#     while open:
#         n = None

#         for v in open:
#             if n==None or g[v]+h[v] < g[n]+h[n]:
#                 n=v
        
#         if n==stop or graph.get(n) == None:
#             pass
#         else:
#             for (neighbour,weight) in graph[n]:
#                 if neighbour not in open and neighbour not in close:
#                     g[neighbour] = weight+g[n]
#                     open.add(neighbour)
#                     parent[neighbour] = n
#                 else:
#                     if g[neighbour] > weight+g[n]:
#                         g[neighbour] = weight+g[n]
#                         parent[neighbour] = n
#                         if neighbour in close:
#                             close.remove(neighbour)
#                             open.add(neighbour)
        
#         if n==None:
#             return
#         if n==stop:
#             path = []
#             while parent[n]!=n:
#                 path.append(n)
#                 n = parent[n]
#             path.append(n)
#             path.reverse()
#             print("Path : ",path)
#             return
#         open.remove(n)
#         close.add(n)


# Astar("A","J")















def AS(start,stop):
    open = set()
    open.add(start)
    closed = set()
    g={}
    parent={}
    g[start] = 0
    parent[start] = start

    while open:
        n=None
        
        for v in open:
            if n==None or g[n]+h[n] > g[v]+h[v]:
                n=v

        if n==stop or graph.get(n) == None:
            pass
        else:
            for nei,nei_c in graph[n]:
                if nei not in closed and nei not in open:
                    open.add(nei)
                    parent[nei] = n
                    g[nei] = nei_c + g[n]
                else:
                    if g[nei] > nei_c+g[n]:
                        g[nei] = nei_c+g[n]
                        parent[nei] = n
                        if nei in closed:
                            closed.remove(nei)
                            open.add(nei)
        
        if n==None:
            return
        
        if n==stop:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            return path
        open.remove(n)
        closed.add(n)


print(AS("A","J"))