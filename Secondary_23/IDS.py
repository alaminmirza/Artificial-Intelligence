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
def ids(graph, start,target):
    depth = 1
    bottom_reached = False
    while not bottom_reached:
        result, bottom_reached = ids_rec(graph,start,target,0,depth)
        if result is not None:
            return result
        depth = depth*2
        print("Increasing depth to " + str(depth))
    return None
def ids_rec(graph,start,target,current_depth,max_depth):
    print(f"visting node {start}")
    if start == target:
        return start, True
    if current_depth == max_depth:
        print("maximum depth reached")
        if not graph.get(start):
            return None, False
        else:
            return None, True
    bottom_reached = True
    for i in graph[start]:
        result,bottom_reached_rec = ids_rec(graph, i,target,current_depth+1,max_depth)
        if result is not None:
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec
    return None, bottom_reached
start=input("Enter root node :")
end=input("Enter goal node :")
ids(graph, start,end)