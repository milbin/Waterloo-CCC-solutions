

def findX(grid):  # this will only work if there are already 2 x values in the grid
    rowValues = {}
    colValues = {}

    # find increment value for rows if exists
    for rowNumber, row in enumerate(grid):
        if row[0] != 'X' and row[1] != 'X':
            rowValues[rowNumber] = int(row[1]) - int(row[0])
        elif row[0] != 'X' and row[2] != 'X':
            rowValues[rowNumber] = int((int(row[2]) - int(row[0]))/2)
        elif row[1] != 'X' and row[2] != 'X':
            rowValues[rowNumber] = int(row[2]) - int(row[1])

    # find increment value for columns if exists
    for colNumber in range(len(grid[0])):  # range(3)
        if grid[0][colNumber] != 'X' and grid[1][colNumber] != 'X':
            colValues[colNumber] = int(grid[1][colNumber]) - int(grid[0][colNumber])
        elif grid[0][colNumber] != 'X' and grid[2][colNumber] != 'X':
            colValues[colNumber] = int((int(grid[2][colNumber]) - int(grid[0][colNumber]))/2)
        elif grid[1][colNumber] != 'X' and grid[2][colNumber] != 'X':
            colValues[colNumber] = int(grid[2][colNumber]) - int(grid[1][colNumber])
    return rowValues, colValues



def populateGrid(rowValues, colValues, oldGrid):
    newGridDict = {0:{0:'X', 1:'X', 2:'X'}, 1:{0:'X', 1:'X', 2:'X'}, 2:{0:'X', 1:'X', 2:'X'}}  # embeded lists represents the rows
    for key, value in rowValues.items():
        row = []
        for i, rowValue in enumerate(grid[key]):  # i represents the index of the known value in the row
            if rowValue != 'X':
                if i == 0:  # known element is the first item
                    row.append(int(rowValue))
                    row.append(int(rowValue) + value)
                    row.append(int(rowValue) + value + value)
                if i == 1:  # known element is the second item
                    row.append(int(rowValue) - value)
                    row.append(int(rowValue))
                    row.append(int(rowValue) + value)
                if i == 2:  # known element is the third item
                    row.append(int(rowValue) - value)
                    row.append(int(rowValue) - value)
                    row.append(int(rowValue))
                break
        for i, value in enumerate(row):
            newGridDict[key][i] = value
    for key, value in colValues.items():  # key is the x value of the current column
        col = []
        for i in range(3):  # i represents the index, or y value, of the known value in the col
            colValue = grid[i][key]
            if colValue != 'X':
                if i == 0:  # known element is the first item
                    col.append(int(colValue))
                    col.append(int(colValue) + value)
                    col.append(int(colValue) + value + value)
                if i == 1:  # known element is the second item
                    col.append(int(colValue) - value)
                    col.append(int(colValue))
                    col.append(int(colValue) + value)
                if i == 2:  # known element is the third item
                    col.append(int(colValue) - value)
                    col.append(int(colValue) - value)
                    col.append(int(colValue))
                break
        for i, value in enumerate(col):
            newGridDict[i][key] = value

    if newGridDict == {0:{0:'X', 1:'X', 2:'X'}, 1:{0:'X', 1:'X', 2:'X'}, 2:{0:'X', 1:'X', 2:'X'}}:
        return oldGrid
    for y, row in enumerate(oldGrid):
        for x, i in enumerate(row):
            if newGridDict[y][x] == 'X' and i != 'X':
                newGridDict[y][x] = i
    newGrid = []
    for rowDict in newGridDict.values():
        row = list(rowDict.values())
        newGrid.append(row)
    return newGrid

def plugInValueForX(grid, recursionDepth, timesFailed):
    rows = {0: 0, 1: 0, 2: 0}  # 2 means even, 1 means odd, -1 means no num, -2 means no x
    cols = {0: 0, 1: 0, 2: 0}
    rowsVal = {0: 0, 1: 0, 2: 0}  # 0 means no num
    colsVal = {0: 0, 1: 0, 2: 0}
    for i, row in enumerate(grid):
        nonXVal = -0.1
        hasX = False
        for x in row:
            if x != 'X':
                nonXVal = int(x)
            else:
                hasX = True
        if hasX:
            if nonXVal == -0.1:  # all x
                rows[i] = -1
            elif nonXVal % 2 == 0:  # even
                rows[i] = 2
                rowsVal[i] = nonXVal
            elif nonXVal % 2 != 0:  # odd
                rows[i] = 1
                rowsVal[i] = nonXVal
        else:
            rowsVal[i] = -2

    for y in range(3):  # y represents the index, or y value, of the known value in the col
        nonXVal = -0.1
        hasX = False
        for x in range(3):  # for item in column
            i = grid[x][y]
            if i != 'X':
                nonXVal = int(i)
            else:
                hasX = True
        if hasX:
            if nonXVal == -0.1:  # all x
                cols[y] = -1
            elif nonXVal % 2 == 0:  # even
                cols[y] = 2
                colsVal[y] = nonXVal
            elif nonXVal % 2 != 0:  # odd
                cols[y] = 1
                colsVal[y] = nonXVal
        else:
            cols[y] = -2

    #print(rows)
    #print(cols)

    newGrid = grid.copy()
    numberOfXsFound = 0
    for y, row in enumerate(grid):
        for x, i in enumerate(row):
            if i == 'X':
                if numberOfXsFound > timesFailed:
                    if rows[y] == 1 and cols[x] == 1:
                        newGrid[y].pop(x)
                        newGrid[y].insert(x, str(rowsVal[y] + recursionDepth))
                        return newGrid
                    elif rows[y] == 2 and cols[x] == 2:
                        newGrid[y].pop(x)
                        newGrid[y].insert(x, str(rowsVal[y] + (2*recursionDepth)))
                        return newGrid
                    elif rows[y] == 0 and cols[x] == 0:
                        newGrid[y].pop(x)
                        newGrid[y].insert(x, str(rowsVal[y] + (2*recursionDepth)))
                        return newGrid
                    elif rows[y] == -1 and cols[x] == -1:
                        newGrid[y].pop(x)
                        newGrid[y].insert(x, str(rowsVal[y] + (2*recursionDepth)))
                        return newGrid
                    else:
                        newGrid[y].pop(x)
                        newGrid[y].insert(x, str(rowsVal[y] + (2 * recursionDepth)))
                        return newGrid
                numberOfXsFound += 1




def checkForX(grid, originalGrid):
    for row in grid:
        for i in row:
            if i == 'X':
                return False
    for y, row in enumerate(originalGrid):
        for x, i in enumerate(row):
            if i != 'X' and i != str(grid[y][x]):
                #print("FAILED")
                return "FAILED"

    finalString = ''
    for row in grid:
        for i in row:
            finalString += str(i)+' '
        finalString += '\n'
    print(finalString)
    return True


import sys
#import time
inputGrid = sys.stdin.read().splitlines()
grid = []
# converts input to a 2d array where elements can be accesses by grid[y][x]
for i, value in enumerate(inputGrid):
    grid.insert(i, value.split(' '))
originalGrid = grid.copy()

timesFailed = -1
recursionDepth = 0
while recursionDepth < 1000:
    rowValues, colValues = findX(grid)
    newGrid = populateGrid(rowValues, colValues, grid)
    if newGrid == grid:
        grid = plugInValueForX(grid, recursionDepth, timesFailed)
    else:
        grid = newGrid.copy()

    result = checkForX(grid, originalGrid)
    if result == "FAILED":
        timesFailed += 1
        grid = originalGrid.copy()
        recursionDepth = -1
    elif result:
        break
    recursionDepth += 1


