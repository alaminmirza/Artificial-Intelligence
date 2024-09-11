def solve(start, end, path=[]):
    dict = {
        'S': ['A', 'B', 'C'],
        'A': ['D', 'E'],
        'B': ['G'],
        'C': ['F'],
        'D': ['H'],
        'E': ['G'],
        'F': ['G'],
        'H': [],
        'G': []
    }


    path = path + [start]

    if start == end:
        return [path]

    if start not in dict:
        return []

    paths = []
    for node in dict[start]:
        if node not in path:
            new_paths = solve(node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths


def UCS(start, end):
    distance = {
        "S": 0,
        "SA": 5,
        "SB": 2,
        "SC": 4,
        "AD": 9,
        "AE": 4,
        "CF": 2,
        "BG": 6,
        "EG": 6,
        "FG": 1,
        "DH": 7
    }

    all_paths = solve(start, end)
    path_cost = []
    while len(all_paths) != len(path_cost):
        temp_array = all_paths[len(path_cost)]
        cost = 0
        for i in range(1, len(temp_array)):
            d = str(temp_array[i - 1]) + str(temp_array[i])
            cost += distance[d]
        path_cost.append(cost)
    shortest = path_cost.index(min(path_cost))
    print("UCS Path :")
    print(all_paths[shortest])
    return print("UCS path cost: " + str(path_cost[shortest]))


if __name__ == '__main__':
    start = str(input("Start Node: "))
    end = str(input("End Node/Goal: "))
    print("")

    print(UCS(start, end))