Graph_nodes = {
        'A': [('B', 5), ('D',2)],
        'B': [('C', 6), ('F', 7)],
        'C': [('E', 4 ), ('G', 9), ('H', 5)],
        'D': [('F', 4)],
        'E': [('B', 1),('F', 3)],
        'F': [('A', 2)],
        'G': [('E', 4), ('H', 6)],
        'H': [('A', 9)]
}

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 10,
        'B': 12,
        'C': 14,
        'D': 7,
        'E': 9,
        'F': 15,
        'G': 6,
        'H': 3
    }
    return H_dist[n]

def aStar (start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {} 
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print("Path does not Exist!")
            return None

        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]
            
            path.append(start_node)
            path.reverse()

            print("\nPath Found: {} \n" .format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not Found!")
    return None

source_node= input("\nEnter the Start Node: ")
goal_node= input("Enter the Goal Node: ")

aStar(source_node, goal_node)
