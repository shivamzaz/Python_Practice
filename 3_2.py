data = []

try:
    File = open('knapsack_big.txt')
    line = File.readline().split()
    weight = int(line[0])
    n = int(line[1])
    for line in File:
        line = line.split()
        data.append((int(line[0]), int(line[1])))
finally:
    File.close()
    
A = [[None for i in range(weight + 1)] for x in range(2)]

for x in range(weight + 1):
    A[0][x] = 0
    
for i in range(1, n + 1):
    if i % 2:
        for x in range(weight + 1):
            if x - data[i - 1][1] >= 0:
                A[1][x] = max(A[0][x], A[0][x - data[i - 1][1]] + data[i - 1][0])
            else:
                A[1][x] = A[0][x]
    else:
        for x in range(weight + 1):
            if x - data[i - 1][1] >= 0:
                A[0][x] = max(A[1][x], A[1][x - data[i - 1][1]] + data[i - 1][0])
            else:
                A[0][x] = A[1][x]
             
if i % 2:
    print(A[1][weight])
else:
    print(A[0][weight])