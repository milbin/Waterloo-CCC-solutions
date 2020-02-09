import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
gridInput = input[1:]
grid = []
for row in gridInput:
    newRow =[]
    for i in row.split(' '):
        newRow.append(int(i))
    grid.append(newRow)


def flipRow(rowNumber, grid):
    newGrid = grid.copy()
    newGrid.pop(rowNumber)
    newRow = []
    for i in grid[rowNumber]:
        if i == 0:
            newRow.append(1)
        else:
            newRow.append(0)
    newGrid.insert(rowNumber, newRow)
    return newGrid

def flipCol(colNumber, grid):
    newCol = []
    for row in grid:
        i = row[colNumber]
        if i == 0:
            newCol.append(1)
        else:
            newCol.append(0)

    newGrid = grid.copy()
    for y in range(len(grid)):
        newGrid[y].pop(colNumber)
    for y in range(len(grid)):
        newGrid[y].insert(colNumber, newCol[y])
    return newGrid

def isSolved(grid):
    allZero = True
    for y in grid:
        for x in y:
            if x == 1:
                allZero = False
    if allZero:
        return True

def getColAt(colNumber):
    col = []
    for y in range(len(grid)):
        col.append(grid[y][colNumber])
    return col
def findRowToFlip(grid):
    N = len(grid)
    numberOfZeros = 0
    while True:
        for i, row in enumerate(grid):
            if sum(row) == N - numberOfZeros:
                return i, numberOfZeros
        numberOfZeros += 1



def findColToFlip(grid):
    numberOfZeros = 0
    N = len(grid)
    while True:
        for i in range(N):
            col = getColAt(i)
            if sum(col) == N - numberOfZeros:
                return i, numberOfZeros
        numberOfZeros += 1




M = 0

movesList = []
if isSolved(grid):
    print(0)
while not isSolved(grid):
    rowToFlip, rowZeros = findRowToFlip(grid)
    colToFlip, colZeros = findColToFlip(grid)
    if rowZeros <= colZeros:
        grid = flipRow(rowToFlip, grid)
        movesList.append('R ' + str(rowToFlip + 1))
        M += 1
    else:
        grid = flipCol(colToFlip, grid)
        movesList.append('C ' + str(colToFlip + 1))
        M += 1

    #import time
    #time.sleep(1)
    #print(grid)
    if isSolved(grid):
        print(M)
        for i in movesList:
            print(i)
        break
    elif M > 1000:
        print('-1')
        break
















