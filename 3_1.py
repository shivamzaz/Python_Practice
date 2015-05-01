data = []

try:
    File = open('knapsack1.txt')
    line = File.readline().split()
    weight = int(line[0])
    n = int(line[1])
    for line in File:
        line = line.split()
        data.append((int(line[0]), int(line[1])))
finally:
    File.close()
    
A = [[None for i in range(weight + 1)] for x in range(n + 1)]

for x in range(weight + 1):
    A[0][x] = 0

for i in range(1, n + 1):
    for x in range(weight + 1):
        if x - data[i - 1][1] >= 0:
            A[i][x] = max(A[i - 1][x], A[i - 1][x - data[i - 1][1]] + data[i - 1][0])
        else:
            A[i][x] = A[i - 1][x]
        
print(A[n][weight])
