data = []
try:
    File = open('jobs.txt')
    n = int(File.readline())  # number of jobs
    for line in File:
        temp = line.split()
        if temp[1]:
            data.append((int(temp[0]), int(temp[1]), float(temp[0]) / float(temp[1])))  # ratio
finally:
    File.close()
    
data = sorted(data, key=lambda data: data[2], reverse=True)  # sort by data[2], decreasing
print(data)
c = int()
Sum = int()

for weight, length, ratio in data:
    c += length
    Sum += c * weight
    
print(Sum)