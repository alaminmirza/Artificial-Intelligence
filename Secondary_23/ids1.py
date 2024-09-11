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

path = list()

def ids(currentNode,destination,graph,maxDepth,curList):
    print("Checking for destination",currentNode)
    curList.append(currentNode)
    if currentNode==destination:
       return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if ids(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False
def iDs(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if ids(currentNode,destination,graph,i,curList):
            return True
    return False
start=input("Enter root node :")
end=input("Enter goal node :")
if not iDs(start,end,graph,4):
    print("Shortest Path is not available")
else:
    print("Shortest path exists")
    print(path.pop())