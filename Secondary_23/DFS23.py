graph = {
  'S' : ['A','B','C'],
  'A' : ['D', 'E'],
  'B' : ['G'],
  'C' : ['F'],
  'D' : ['H'],
  'E' : ['G'],
  'F' : ['G'],
  'G' : [],
  'H' : []
}

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for neighbour in graph[start]:
        if neighbour  not in path:
            newpath = dfs(graph, neighbour, end, path)
            if newpath: 
                return newpath
    return None

def shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for neighbour  in graph[start]:
        if neighbour not in path:
            newpath = shortest_path(graph, neighbour, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

root = input("\nEnter root node: ")
goal = input("Enter Goal node: ")

temp = []
temp = shortest_path(graph, root, goal)
print("\nShortest Path: ", shortest_path(graph, root, goal))
print("\n")