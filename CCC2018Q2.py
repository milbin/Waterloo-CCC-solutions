N = int(input())
sunflowers = []
for i in range(N):
    temp = []
    for x in input().split(' '):
        temp.append(int(x))
    sunflowers.append(temp)



def rotate(sunflowers, N):
    newSunflowers = []
    for i in range(N):
        TEMP = []
        for x in range(N):
            TEMP.append(sunflowers[N-1-x][i])
        newSunflowers.append(TEMP)
    return newSunflowers
sunflowers = rotate(sunflowers, N)

found = False
numberofruns = 0
while not found:
    rotated = False
    for sunflower in sunflowers:
        good = True
        for i in range(N):
            try:
                if sunflower[i] >= sunflower[i+1]:
                    sunflowers = rotate(sunflowers, N)
                    rotated = True
                    good = False
                    break
            except:
                pass
        if not rotated:
            found = True

    sunflowerCollums = []
    if not rotated:
        for i in range(N):
            temp = []
            for x in range(N):
                temp.append(sunflowers[x][i])
            sunflowerCollums.append(temp)
        #print(sunflowerCollums)

        good = True
        for coll in sunflowerCollums:
            if coll[0] != min(coll):
                sunflowers = rotate(sunflowers, N)
                rotated = True
                good = False
                break
        if good:
            found = True
    numberofruns +=1





printList = []
for sunflower in sunflowers:
    string = ''
    for i in sunflower:
        string+= str(i)+' '

    printList.append(string)

for i in printList:
    print(i)



