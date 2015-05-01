data = []
try:
    File = open('jobs.txt')
    n = int(File.readline())  # number of jobs
    for line in File:
        temp = line.split()
        if temp[1]:
            data.append((int(temp[0]), int(temp[1]), int(temp[0]) - int(temp[1])))  # diff
finally:
    File.close()
    
data = sorted(data, key=lambda data: data[0], reverse=True)  # sort by data[0], decreasing
data = sorted(data, key=lambda data: data[2], reverse=True)  # sort by data[2], decreasing

c = int()
Sum = int()

for weight, length, diff in data:
    c += length
    Sum += c * weight
    
print(Sum)
