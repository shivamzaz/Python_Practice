data = {}   
try:
    file = open("dijkstraData.txt")
    for line in file:
        temp = line.split()
        for i in range(len(temp[1:])):
            temp[i + 1] = temp[i + 1].split(',')
            temp[i + 1] = (int(temp[i + 1][0]), int(temp[i + 1][1]))
        data[int(temp[0])] = temp[1:]  #dictionary: vertex to pairs (other vertex, weight)
finally:
    file.close()

#DIJKSTRA (n * m)
X = [1]  #starts from 1 vertex
A = {} 

for i in data:
    A[i] = 1000000
    
A[1] = 0

temp = []
while len(X) != len(data):
    i = X[-1]
    temp += [(k, A[i] + l) for k, l in data[i] if not k in X]
    temp.sort(key = lambda tup: tup[1])
    A[temp[0][0]] = temp[0][1]
    X.append(temp[0][0])
    for k, l in temp:
        if k == X[-1]:
            temp.remove((k,l))

for i in [7,37,59,82,99,115,133,165,188,197]:
    print(i, A[i])