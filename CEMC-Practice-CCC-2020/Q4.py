import sys
input = sys.stdin.read().splitlines()
M = int(input[0])

pens = {}
allEdges = {}
penCount = 0
for dataString in input[1:]:
    tempEdges = []
    tempWeights = []
    data = dataString.split(' ')
    edgeCount = int(data[0])
    for i in range(1, edgeCount):
        edge = sorted((data[i], data[i+1]))
        tempEdges.append(edge)
    lastEdge = sorted((data[1], data[edgeCount]))
    tempEdges.append(lastEdge)

    for i in data[edgeCount+1:]:
        tempWeights.append(int(i))
    for i, edge in enumerate(tempEdges):
        allEdges[tuple(edge)] = tempWeights[i]
    for edge in tempEdges:
        if pens.get(tuple(edge), False):
            pens[tuple(edge)] += 1
        else:
            pens[tuple(edge)] = 1
    penCount += 1

for key, value in pens.items():
    if pens[key] == 1:
        pens[key] = 2


#print(sorted(list(allEdges.values())))
totalCost = 0

for move in range(M):
    lowestWeight = 100000000
    bestEdgeToRemove = None
    for i, edge in enumerate(list(allEdges.keys())):
        weight = allEdges[edge]
        newWeight = pens[edge] * weight
        if newWeight < lowestWeight:
            lowestWeight = newWeight
            bestEdgeToRemove = edge
    totalCost += allEdges[bestEdgeToRemove]
    #print(bestEdgeToRemove)
    #print(lowestWeight)
    allEdges.pop(bestEdgeToRemove)
    pens.pop(bestEdgeToRemove)
print(totalCost)



