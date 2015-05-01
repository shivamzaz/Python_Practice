data = {}
try:
    count = int()
    File = open('clustering_big.txt')
    temp = File.readline().split()
    n = int(temp[0])
    n_bits = int(temp[1])
    for line in File:
        count += 1
        temp = line.split()
        data[count] = [int(i) for i in temp]
finally:
    File.close()

def difference(first, second, n_bits):
    counter = int()
    for i in range(n_bits):
        if first[i] != second[i]:
            counter += 1
    return counter  

clusters = int()
to_use = [i for i in range(1, n + 1)]
clusterList = {}  # dict of clusters - only numbers (indexes of data)
 
while to_use:
    for i in to_use:
        to_use.remove(i)
        clusters += 1
        clusterList[i] = [i]
        count = 0
        while count < len(clusterList[i]):
            temp = clusterList[i][count]
            for j in to_use:
                if difference(data[temp], data[j], n_bits) <= 2:
                    clusterList[i].append(j)
                    to_use.remove(j)
            count += 1
                 
print(clusters)