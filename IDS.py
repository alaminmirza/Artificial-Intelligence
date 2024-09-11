def IDS(start, end):
    depth = 0
    while True:
        print ("\nLooping at Depth %i " % (depth))
        result = DFS(start, end, depth)
        print ("Result: %s, Goal: %s \n" % (result, end))
        if result == end:
            return result
        depth = depth +1

def DFS(start, end, depth):
    print ("Start: %s, End %s, Depth: %i" % (start, end, depth))
    if depth == 0 and start == end:
        print ("\n--- Found Goal, Returning ---")
        return start
    elif depth > 0:
        print ("Looping through Children: %s" % (graph.get(start, [])))
        for child in graph.get(start, []):
            if goal == DFS(child, goal, depth-1):
                path.append(child)
                return goal

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
path = []

IDS(source, goal)

path.append(source)
path.reverse()
print("Shortest Path: ", path)
print("\n")

print("Path Cost: ", path_cost(path))
print("\n")