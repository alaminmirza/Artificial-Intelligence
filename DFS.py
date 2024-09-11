#dfs

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath: 
                return newpath
    return None


def all_possible_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = all_possible_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def path_cost(temp):

    a1=0
    a2=0
    cost=0

    while temp:

        a1=temp.pop(0)

        if a2=='A' and a1=='D':
            cost=cost+2

        if a2=='A' and a1=='B':
            cost=cost+3

        if a2=='B' and a1=='C':
            cost=cost+2

        if a2=='B' and a1=='F':
            cost=cost+1

        if a2=='C' and a1=='E':
            cost=cost+1

        if a2=='C' and a1=='G':
            cost=cost+1

        if a2=='C' and a1=='H':
            cost=cost+4

        if a2=='D' and a1=='F':
            cost=cost+3

        if a2=='E' and a1=='B':
            cost=cost+3

        if a2=='E' and a1=='F':
            cost=cost+2

        if a2=='F' and a1=='A':
            cost=cost+5

        if a2=='F' and a1=='B':
            cost=cost+1

        if a2=='G' and a1=='E':
            cost=cost+2

        if a2=='G' and a1=='H':
            cost=cost+3

        if a2=='H' and a1=='A':
            cost=cost+5

        a2=a1

    return cost


graph = {
        'A': ['B', 'D'],
        'B': ['C', 'F'],
        'C': ['E', 'G', 'H'],
        'D': ['F'],
        'E': ['B','F'],
        'F': ['A'],
        'G': ['E', 'H'],
        'H': ['A']
        }


source = input("\nSet Source: ")
goal = input("Set Goal: ")

temp = []
temp = shortest_path(graph, source, goal)

print("\nBasic DFS: ", dfs(graph, source, goal))
print("\nPossible Paths: ", all_possible_paths(graph, source, goal))
print("\nShortest Path: ", shortest_path(graph, source, goal))
print("\nShortest Path Cost: ", path_cost(temp))
print("\n")