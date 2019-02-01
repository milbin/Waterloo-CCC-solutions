

N = int(input())
villages = []
for i in range(N):
    villages.append(int(input()))

villages = sorted(villages)

midpoints = []
for i in range(len(villages)):
    try:
        midpoints.append((villages[i] + villages[i+1])/2)
    except:
        pass


smallestVillage = midpoints[1] - midpoints[0]
for i in range(len(midpoints)):
    try:
        if midpoints[i+1] - midpoints[i] <= smallestVillage:
            smallestVillage = midpoints[i+1] - midpoints[i]
    except:
        pass

print(round(smallestVillage, 4))


