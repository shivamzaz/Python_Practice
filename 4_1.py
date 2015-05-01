infinity = 10000000

actualFile = 'g3.txt'

try:
    File = open(actualFile)
    temp = File.readline().split()
    n, m = int(temp[0]), int(temp[1])
    data = [{} for i in range(n)]
    for line in File:
        temp = line.split()
        a, b, d = int(temp[0]), int(temp[1]), int(temp[2])
        data[b - 1][a - 1] = d
finally:
    File.close()

# data [i] is a dictionary, data[i][j] is the cost of edge (i - 1, j - 1)

#===============================================================================
# The Floyd-Warshall Algorithm
#===============================================================================

A = [[[None, None] for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            A[i][j][0] = 0
        elif j in data[i].keys():
            A[i][j][0] = data[i][j]
        else:
            A[i][j][0] = infinity

for k in range(1, n):
    for i in range(n):
        for j in range(n):
            t = k % 2
            A[i][j][t] = min(A[i][j][(t + 1) % 2], A[i][k][(t + 1) % 2] + A[k][j][(t + 1) % 2])
            
#===============================================================================
# Check for negative cycle
#===============================================================================
            
flag = False
for i in range(n):
    if A[i][i][(n - 1) % 2] < 0:
        flag = True 
        
#===============================================================================
# Calculating shortest path's length
#===============================================================================

minimum = infinity
if not flag:
    for i in range(n):
        for j in range(n):
            if i != j and A[i][j][(n - 1) % 2] < minimum:
                minimum = A[i][j][(n - 1) % 2]
            
print(minimum)
