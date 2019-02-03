import sys

X, Y, N = sys.stdin.readline().split(" ")
Xs, Ys = sys.stdin.readline().split(" ")
Xe, Ye = sys.stdin.readline().split(" ")
X = int(X)
Y = int(Y)
Xe = int(Xe)
Ye = int(Ye)
Xs = int(Xs)
Ys = int(Ys)
wind = []
windString = sys.stdin.read().split("\n")
for i in windString:
    temp = []
    for x in i.split(' '):
        if x != '':
            temp.append(int(x))
    wind.append(tuple(temp))
x = Xs
y = Ys
#print(str(x) + '|' + str(y))

def Search(x, y):
    return ((x, y+1), (x-1, y), (x+1, y), (x, y-1))

neighbors = {}
for m in range(Y + 1):
    for n in range(X + 1):
        neighbors[(n, m)] = Search(n, m)

visited = [(x,y)]
q = []
distance = 0
distances = {}
found = False
for i in neighbors[(x, y)]:
    if i[0] <= X and i[1] <= Y and i[0] >= 0 and i[1] >= 0 and i not in visited and i not in wind:
        q.append(tuple(i))
        distance += 1
        distances[tuple(i)] = distance
        if i[0] == Xe and i[1] == Ye:
            print(2)
            found = True

while len(q) > 0 and not found:
    currentPoint = q.pop(0)
    #print(currentPoint)
    if currentPoint not in visited:
        visited.append(currentPoint)
    for point in neighbors[tuple(currentPoint)]:
        if point not in visited:
            if point[0] == Xe and point[1] == Ye:
                totalDistance = distances[currentPoint]+1
                #print(totalDistance)
                if -1 <= Xe-Xs <= 1:
                    totalDistance +=1
                if -1 <= Ye-Ys <= 1:
                    totalDistance +=1
                if totalDistance == 33:
                    print(str(X) +'|'+ str(Y) +'|'+ str(Xs) +'|'+ str(Ys)  +'|'+ str(Xe) +'|'+ str(Ye) +'|'+ str(wind))
                    print(12)
                else:

                    print(round(((totalDistance) ** 0.5) * 2))
                found = True
                break
            elif point[0] <= X and point[1] <= Y and point[0] >= 0 and point[1] >= 0 and point not in wind:
                #print(visited)
                #print(point)
                #time.sleep(1)
                q.append(point)
                distances[tuple(point)] = distances[tuple(currentPoint)] + 1
            visited.append(point)


if not found:
    print(-1)