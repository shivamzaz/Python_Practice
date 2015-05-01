class Node:
    def __init__(self, out, out_rev, t, explored):
        self.out = out
        self.out_rev = out_rev
        self.t = t
        self.exp = explored
        
    def __repr__(self):
        return str(self.t) + str(self.exp)
    
    def __str__(self):
        return 'out: ' + str(self.out) + '\n' + str(self.t) + str(self.exp)

### recursively for small data ###
def DFS_loop_rec(G, by_time):  # expect G - dictionary of nodes
    global source_vertex
    global Time
    if not by_time:
        for i in G:
            if not G[i].exp:
                DFS_rec(G, i, by_time)
    else:
        while Time:
            for i in G:
                if G[i].t == Time:
                    if not G[i].exp:
                        source_vertex = i
                        DFS_rec(G, i, by_time)
                    else:
                        break
            Time -= 1
    return

def DFS_rec(G, i, by_time):
    global SCCs
    global source_vertex
    global Time
    G[i].exp = True
    if by_time:
        if SCCs.has_key(source_vertex):
            SCCs[source_vertex] += [i]
        else:
            SCCs[source_vertex] = [i]
        for j in G[i].out:
            if not G[j].exp:
                DFS_rec(G, j, by_time)
    if not by_time:
        for j in G[i].out_rev:
            if not G[j].exp:
                DFS_rec(G, j, by_time)
        Time += 1
    G[i].t = Time
    return
####################################

### iterative - for big data ###
def DFS_iter(G):
    stack = []
    list_by_time = []
    Time = 0
    for i in G:
        if not G[i].exp:
            stack.append(i)
            G[i].exp = True
            while stack:
                temp = stack[-1]
                flag = True
                while flag:
                    flag = False
                    temp = stack[-1]
                    for j in G[temp].out_rev:
                        if not G[j].exp:
                            stack.append(j)
                            G[j].exp = True
                            flag = True
                            break
                Time += 1
                G[temp].t = Time
                stack.remove(temp)
                list_by_time.append(temp)
    list_by_time.reverse()
    SCCs = {}
    stack = []
    for i in G:
        G[i].exp = False
    print("polowa")
    for i in list_by_time:
        if not G[i].exp: 
            SCCs[i] = []
            stack.append(i)
            G[i].exp = True
            while stack:
                temp = stack[-1]
                flag = True
                while flag:
                    flag = False
                    temp = stack[-1]
                    for j in G[temp].out:
                        if not G[j].exp:
                            stack.append(j)
                            G[j].exp = True
                            flag = True
                            break
                SCCs[i].append(temp)
                stack.remove(temp)
    return SCCs
    

data = {}  # graph
try:
    file = open('SCC.txt')  # read the file
    for line in file:
        temp = line.split()
        if not data.has_key(int(temp[0])):
            data[int(temp[0])] = Node([int(temp[1])], [], int(), False)
        else:
            data[int(temp[0])].out += [int(temp[1])]
        if data.has_key(int(temp[1])):  # #makes list with endings of edges from this vertex, but reverse arcs
            data[int(temp[1])].out_rev += [int(temp[0])]
        else: 
            data[int(temp[1])] = Node([], [int(temp[0])], int(), False)
finally:
    file.close()


SCCs = DFS_iter(data)
print("sort")
maxims = [0, 0, 0, 0, 0]
for i in SCCs:
    if len(SCCs[i]) > min(maxims):
        maxims[maxims.index(min(maxims))] = len(SCCs[i])
print(maxims)

'''
### recursively for small data ###   
SCCs = {}  #here is scc dictionary (leader and other vertices)
Time = int()
source_vertex = int()

DFS_loop_rec(data, False)
for i in data:
    data[i].exp = False
DFS_loop_rec(data, True)
print(SCCs)
#################################
'''