import sys
import math

input = sys.stdin.read().splitlines()
baseOfTriangle = int(input[0].split(' ')[0])
baseOfSubTriangle = int(input[0].split(' ')[1])
input.pop(0)
triangle  = []
for vertex in input:
    triangle.append(vertex.split(' '))

pointAtVertex = {}
neighbors = {}
for y, row in enumerate(triangle):
    for x, vertex in enumerate(row):
        try:
            neighbors[(x, y)]
        except:
            neighbors[(x, y)] = {}

        pointAtVertex[(x, y)] = vertex
        if y+1 < baseOfTriangle and x >= 0:
            neighbors[(x, y)]['bottom left'] = (x, y+1)  # bottom left
        if x+1 <= y+1 and y+1 < baseOfTriangle:
            neighbors[(x, y)]['bottom right'] = (x+1, y+1)  # bottom right

print("HERE")
if baseOfSubTriangle == 1:
    total = 0
    for point in list(pointAtVertex.values()):
        total += int(point)
    print(total)
    exit()


def getNeighbors(vertex):
    neighborsList = []
    try:
        neighborsList.append(neighbors[vertex]['bottom right'])
    except:
        pass
    try:
        neighborsList.append(neighbors[vertex]['bottom left'])
    except:
        pass
    return neighborsList


def generateTriangleOfSize(triangleDepth, point):
    subTriangleVerticies = [point]
    for vertex in subTriangleVerticies:
        depth = 0
        a = 1
        b = 1
        c = len(subTriangleVerticies)
        x1 = -1
        x2 = -1
        try:
            x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        except:
            pass
        try:
            x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
        except:
            pass
        if x1 > 0:
            depth = x1
        elif x2 > 0:
            depth = x2
        print(x1)
        print(x2)
        import time
        time.sleep(1)
        if depth == triangleDepth:
            print('found sub')
            return sorted(subTriangleVerticies)


        twoNeighbors = getNeighbors(vertex)
        if len(twoNeighbors) == 2:
            for neighbor in getNeighbors(vertex):
                subTriangleVerticies.append(neighbor)
        else:
            return []





totalPoints = 0
print(len(list(pointAtVertex.keys())))
for vertex in list(pointAtVertex.keys()):
    subTriangle = generateTriangleOfSize(baseOfSubTriangle, vertex)
    if len(subTriangle) != 0 :
        totalPoints += int(max(subTriangle))
print(totalPoints)

