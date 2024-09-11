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

def bfs(graph, start, end):
  queue = [] 
  queue.append(start)

  while queue:
    p = queue.pop(0) 
    print (p, end = " ") 
    node = p[-1]
    if node == end:
        return p
    for adjacent in graph.get(node, []):
            new_path = list(p)
            new_path.append(adjacent)
            queue.append(new_path)

start=input("Enter root node :")
end=input("Enter goal node :")
bfs (graph, start, end)