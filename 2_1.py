data = []
try:
    File = open('clustering1.txt')
    n = int(File.readline())
    for line in File:
        temp = line.split()
        data.append((int(temp[0]), int(temp[1]), int(temp[2])))
finally:
    File.close()
    
clusters = [[i] for i in range(1, n + 1)]
data = sorted(data, key = lambda data: data[2])
 
while len(clusters) > 4:  # k = 4
    for i in clusters:
        if data[0][0] in i and data[0][1] not in i:
            for j in clusters:
                if data[0][1] in j:
                    i += j
                    clusters.remove(j)
                    break
            break
        elif data[0][1] in i and data[0][0] not in i:
            for j in clusters:
                if data[0][0] in j:
                    i += j
                    clusters.remove(j)
                    break
            break
    data.pop(0)
   
print(clusters)

flag = False
for i in range(len(data)):
    for j in clusters:
        if (data[i][0] in j and data[i][1] not in j) or (data[i][1] in j and data[i][0] not in j):
            print(data[i][2])
            flag = True
            break
    if flag:
        break
            