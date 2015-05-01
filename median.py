data = []
Sum = int()
i = int()
try:
    File = open("Median.txt")
    for line in File:
        i += 1
        flag = False
        for j in range(len(data)):
            if data[j] >= int(line):
                data.insert(j, int(line))
                flag = True
                break
        if not flag:
                data.append(int(line))
        if i % 2 == 1:
            Sum += data[(i + 1)/2 - 1]
        else:
            Sum += data[i/2 - 1]
finally:
    File.close()
    
print(Sum % 10000)