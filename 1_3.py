data = {}
try:
    File = open('edges.txt')
    temp = File.readline().split()
    n = int(temp[0])  # number of vertices
    m = int(temp[1])  # number of edges
    for line in File:
        temp = line.split()
        if temp[2]:
            if int(temp[0]) in data.keys():
                data[int(temp[0])] += [(int(temp[1]), int(temp[2]))]
            else:
                data[int(temp[0])] = [(int(temp[1]), int(temp[2]))]
            if int(temp[1]) in data:
                data[int(temp[1])] += [(int(temp[0]), int(temp[2]))]
            else:
                data[int(temp[1])] = [(int(temp[0]), int(temp[2]))]
finally:
    File.close()

spanned_ver = [data[1][0][0]]
Sum = int()

for i in data.keys():
    temp = data[i]
    data[i] = sorted(temp, key=lambda temp: temp[1])

while not sorted(spanned_ver) == data.keys():
    temp = []
    for i in spanned_ver:
        for j in data[i]:
            if j[0] not in spanned_ver:
                temp.append(j)
                break
    temp = sorted(temp, key = lambda temp: temp[1])
    spanned_ver.append(temp[0][0])
    Sum += temp[0][1]
    
print(Sum)