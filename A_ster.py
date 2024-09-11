from queue import Queue
import copy

tree = {
    'S':{'A','B','E'},
    'A':{'C','B','S'},
    'B':{'D','S','G'},
    'C':{'G','A'},
    'D':{'E','B'},
    'E':{'G','D','A'},
    'G':{'B','C','E'},
}

Edge = {
    1:{'S','A'},
    2:{'S','B'},
    3:{'A','B'},
    4:{'A','C'},
    5:{'B','D'},
    6:{'C','G'},
    7:{'D','E'},
    8:{'E','G'},
    9:{'G','B'},
    10:{'S','E'}
}
cost ={
    1:3,
    2:2,
    3:5,
    4:2,
    5:4,
    6:5,
    7:1,
    8:2,
    9:3,
    10:1
    
}

hur = {
    'S':15,
    'A':12,
    'B':11,
    'C':9,
    'D':4,
    'E':2,
    'G':10,
}

pcost = {}
hcost = []
parent = {}
visited = {}
aa = []
queue = Queue()
q2= []
temp = []
tcost = 0

for node in tree.keys():
    visited[node]=False
    parent[node] = None
s = 'S'
goal = input("Enter goal = ")
visited[s] = True
pcost[s] = 0
cc = 0
pc = 0
queue.put(s)
q2.append(s)
ou=1
while not queue.empty():
    u =queue.get()
    index = q2.index(u)
    q2.pop(index)
    aa.append(u)
    pc = copy.deepcopy(pcost[u]) 
    outt = 0
    
    for v in tree[u]:
        if not visited[v]:
            print(v)
            if v == goal:
                aa.append(goal)
                ou = 0
                for edge in Edge.keys():
                    if v in Edge[edge] and u in Edge[edge]:
                        cc = cost[edge]
                pcost[v] = pc + cc
                tcost = pc + cc
                break
            visited[v] = True
            parent[v] =  u
            for edge in Edge.keys():
                if v in Edge[edge] and u in Edge[edge]:
                    cc = cost[edge]
            pcost[v] = pc + cc
            tcost = pc + cc
            hp = pcost[v] + hur[v]
            hcost.append(hp)
            temp.append(v)
            q2.append(v)
            outt = 1
    if ou == 0:
        break
    if outt == 0:
        
        for ss in q2:
            queue.put(ss)
    else:
        val, idx = min((val, idx) for (idx, val) in enumerate(hcost))
        queue.put(temp[idx])
        temp.clear()
        hcost.clear()
        print(list(queue.queue))
               
print(hcost)  
print(aa)
print(tcost)