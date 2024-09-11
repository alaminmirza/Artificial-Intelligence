import timeit
from collections import deque

#Global variables

GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
GoalNode = None     # at finding solution
NodesExpanded = 0   # total nodes visited
MaxSearchDeep = 0   # max deep
MaxFrontier = 0     # max frontier



#Information

class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
    def __str__(self):
        return str(self.map)



#Obtain Sub Nodes

def subNodes(node):

    global NodesExpanded
    NodesExpanded = NodesExpanded+1

    nextPaths = []
    nextPaths.append(PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for procPaths in nextPaths:
        if(procPaths.state!=None):
            nodes.append(procPaths)
    return nodes



#BFS

def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited= set()
    Queue = deque([PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = subNodes(node)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize



#A-Star

def ast(startState):
    
    global MaxFrontier, MaxSearchDeep, GoalNode
    
    #transform initial state to calculate Heuritic
    node1 = ""
    for poss in startState:
        node1 = node1 + str(poss)

    #calculate Heuristic and set initial node
    key = Heuristic(node1)
    boardVisited= set()
    Queue = []
    Queue.append(PuzzleState(startState, None, None, 0, 0, key)) 
    boardVisited.add(node1)
    
    while Queue:
        Queue.sort(key=lambda o: o.key) 
        node = Queue.pop(0)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = subNodes(node)
        for path in posiblePaths:      
            thisPath = path.map[:]
            if thisPath not in boardVisited:
                key = Heuristic(path.map)
                path.key = key + path.depth
                Queue.append(path)               
                boardVisited.add(path.map[:])
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep
        


#Heuristic: distance to root numbers
values_0 = [0,1,2,1,2,3,2,3,4]
values_1 = [1,0,1,2,1,2,3,2,3]
values_2 = [2,1,0,3,2,1,4,3,2]
values_3 = [1,2,3,0,1,2,1,2,3]
values_4 = [2,1,2,1,0,1,2,1,2]
values_5 = [3,2,1,2,1,0,3,2,1]
values_6 = [2,3,4,1,2,3,0,1,2]
values_7 = [3,2,3,2,1,2,1,0,1]
values_8 = [4,3,2,3,2,1,2,1,0]

def Heuristic(node):

    global values_0,values_1,values_2,values_3,values_4,values_5,values_6,values_7,values_8   
    v0=values_0[node.index("0")]
    v1=values_1[node.index("1")]
    v2=values_2[node.index("2")]
    v3=values_3[node.index("3")]
    v4=values_4[node.index("4")]
    v5=values_5[node.index("5")]
    v6=values_6[node.index("6")]
    v7=values_7[node.index("7")]
    v8=values_8[node.index("8")]
    valorTotal = v0+v1+v2+v3+v4+v5+v6+v7+v8
    return valorTotal



#Next Step

def move(state, direction):

    #generate a copy
    newState = state[:]

    #obtain poss of 0
    index = newState.index(0)

    if(index==0):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[0]
            newState[0]=newState[3]
            newState[3]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[0]
            newState[0]=newState[1]
            newState[1]=temp
        return newState      
    if(index==1):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[1]
            newState[1]=newState[4]
            newState[4]=temp
        if(direction==3):
            temp=newState[1]
            newState[1]=newState[0]
            newState[0]=temp
        if(direction==4):
            temp=newState[1]
            newState[1]=newState[2]
            newState[2]=temp
        return newState    
    if(index==2):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[2]
            newState[2]=newState[5]
            newState[5]=temp
        if(direction==3):
            temp=newState[2]
            newState[2]=newState[1]
            newState[1]=temp
        if(direction==4):
            return None
        return newState
    if(index==3):
        if(direction==1):
            temp=newState[3]
            newState[3]=newState[0]
            newState[0]=temp
        if(direction==2):
            temp=newState[3]
            newState[3]=newState[6]
            newState[6]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[3]
            newState[3]=newState[4]
            newState[4]=temp
        return newState
    if(index==4):
        if(direction==1):
            temp=newState[4]
            newState[4]=newState[1]
            newState[1]=temp
        if(direction==2):
            temp=newState[4]
            newState[4]=newState[7]
            newState[7]=temp
        if(direction==3):
            temp=newState[4]
            newState[4]=newState[3]
            newState[3]=temp
        if(direction==4):
            temp=newState[4]
            newState[4]=newState[5]
            newState[5]=temp
        return newState
    if(index==5):
        if(direction==1):
            temp=newState[5]
            newState[5]=newState[2]
            newState[2]=temp
        if(direction==2):
            temp=newState[5]
            newState[5]=newState[8]
            newState[8]=temp
        if(direction==3):
            temp=newState[5]
            newState[5]=newState[4]
            newState[4]=temp
        if(direction==4):
            return None
        return newState
    if(index==6):
        if(direction==1):
            temp=newState[6]
            newState[6]=newState[3]
            newState[3]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[6]
            newState[6]=newState[7]
            newState[7]=temp
        return newState
    if(index==7):
        if(direction==1):
            temp=newState[7]
            newState[7]=newState[4]
            newState[4]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[7]
            newState[7]=newState[6]
            newState[6]=temp
        if(direction==4):
            temp=newState[7]
            newState[7]=newState[8]
            newState[8]=temp
        return newState
    if(index==8):
        if(direction==1):
            temp=newState[8]
            newState[8]=newState[5]
            newState[5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[8]
            newState[8]=newState[7]
            newState[7]=temp
        if(direction==4):
            return None
        return newState



#Build initial board state
source = []
print("\nInput the Puzzle:")
for i in range(0, 9):
    element = int(input())
    source.append(element)

#Start the Operation
start = timeit.default_timer()

#Run the Operation
print("\n(1) BFS\n(2) A-star\n")
option = input("Chose Option: ")
if option == '1':
    print("\nRunning BFS Algorithm....")
    print("\nPuzzle: ",source)
    print("Goal: ", GoalState)
    bfs(source)

elif option == '2':
    print("\nRunning A-star Algorithm....")
    print("\nPuzzle: ",source)
    print("Goal: ", GoalState)
    ast(source)

stop = timeit.default_timer()
time = stop-start

#Save total path result
deep=GoalNode.depth
moves = []
while source != GoalNode.state:
    if GoalNode.move == 1:
        path = 'Up'
    if GoalNode.move == 2:
        path = 'Down'
    if GoalNode.move == 3:
        path = 'Left'
    if GoalNode.move == 4:
        path = 'Right'
    moves.insert(0, path)
    GoalNode = GoalNode.parent


#Print results
print("\nMoves to the Solve: ",moves)
print("\nTotal Moves: ",len(moves))
print("Total Nodes Expanded: ",str(NodesExpanded))
print("Search Runtime: ",format(time, '.8f'),"sec\n")


#Generate a Text File with Solution
file= open('Result.txt', 'w')
file.write("Puzzle: " + str(source) + "\n")
file.write("Goal: " + str(GoalState) + "\n")
file.write("\n")
file.write("Moves to Solve: " + str(moves) + "\n")
file.write("\n")
file.write("Total Moves: " + str(len(moves)) + "\n")
file.write("Total Nodes Expanded: " + str(NodesExpanded) + "\n")
file.write("Search Depth: " + str(deep) + "\n")
file.write("Max Search Depth: " + str(MaxSearchDeep) + "\n")
file.write("Search Runtime: " + format(time, '.8f') + " sec" + "\n")
file.close()