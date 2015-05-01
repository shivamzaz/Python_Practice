data = {}
try:
    File = open('2sum.txt')
    for line in File:
        data[int(line)] = int(line)
finally:
    File.close()
    
counter = 0   #int()
for t in range(-10000, 10001):
    for i in data:
        if t - i in data:
            counter += 1
            break



print(counter)
#427
