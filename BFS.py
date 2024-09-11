graph = {
        'A': ['B', 'E', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
        }

source = input("Input Source: ")
goal = input("Input Goal: ")


def BFS_SP(graph, start, end):
    explored = []

    queue = [[start]]

    if start == end:
        print("Same Node")
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]
                
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end:
                    return new_path
            explored.append(node)

    print("Path doesn't Exist")
    return

temp = []
temp = BFS_SP(graph, source, goal)
print("Shortest Path: ", *temp)

a1=0
a2=0
cost=0

while temp:

    a1=temp.pop(0)

    if a2=='A' and a1=='B':
        cost=cost+1
    if a2=='B' and a1=='A':
        cost=cost+1

    if a2=='A' and a1=='E':
        cost=cost+2
    if a2=='E' and a1=='A':
        cost=cost+2

    if a2=='A' and a1=='C':
        cost=cost+4
    if a2=='C' and a1=='A':
        cost=cost+4

    if a2=='B' and a1=='D':
        cost=cost+2
    if a2=='D' and a1=='B':
        cost=cost+2

    if a2=='B' and a1=='E':
        cost=cost+3
    if a2=='E' and a1=='B':
        cost=cost+3

    if a2=='C' and a1=='F':
        cost=cost+6
    if a2=='F' and a1=='C':
        cost=cost+6

    if a2=='C' and a1=='G':
        cost=cost+7
    if a2=='G' and a1=='C':
        cost=cost+7

    if a2=='D' and a1=='E':
        cost=cost+5
    if a2=='E' and a1=='D':
        cost=cost+5

    a2=a1

print("Path Cost: ", cost)