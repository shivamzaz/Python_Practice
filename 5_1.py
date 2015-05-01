#from numpy.lib.scimath import sqrt
import math

data = []

#===============================================================================
# Reading data from file, every tuple is (x,y) of point
#===============================================================================
try:
    File = open('tsp.txt')
    n = int(File.readline())
    for line in File:
        temp = line.split()
        data.append((float(temp[0]), float(temp[1])))
finally:
    File.close()
    
#===============================================================================
# A Dynamic Programming Algorithm for TSP
#===============================================================================
inf = 100000
n = 5
# creating table of costs
costs = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        costs[i][j] = ((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2)**(1/2)

data = None

List = [i + 1 for i in range(0, 2 ** n - 1)]
 
def countOnesInBinary(num):
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num = num // 2    
    return count
 
def getSet(num):
    count = 0
    temp = {1}
    while num > 0:
        if num % 2 == 1:
            temp.add(List[count])
        count += 1
        num = num // 2
    return temp
 
def getIndexOfSet(setArg):
    result = 0
    for i in setArg:
        result += 2 ** (i - 1)
    return result
 
A = [{} for i in range(2 ** n)]  # number of subsets containing 1 is 2^(n-1)
      
for i in range(2 ** n):
    A[i][0] = inf
A[0][0] = 0
     
for m in range(2, n + 1):
    for i in List: 
        if countOnesInBinary(i) == m:
            temp = getSet(i)
            for k in temp:
                if k != 1:
                    thirdTemp = getIndexOfSet(temp - {k})
                    print(thirdTemp - 1)
                    secondTemp = {A[thirdTemp - 1][j - 1] + costs[j - 1][k - 1] for j in temp if k != j}
                    A[i - 1][k - 1] = min(secondTemp)
for i in range(len(A)):
    print(i, A[i])
print(min({A[getIndexOfSet(set(range(1, n + 1))) - 1][j] + costs[j][0] for j in range(1, n)}))
 
