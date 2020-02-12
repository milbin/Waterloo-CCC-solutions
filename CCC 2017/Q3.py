import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
boardsInput = input[1].split(' ')
boards = []
for board in boardsInput:
    boards.append(int(board))

boards = sorted(boards)
boardsRemainingCopy = {}
for board in boards:
    boardsRemainingCopy[board] = boards.count(board)

maxLenOfFence = int(boards[-1]*2)
solutions = {}
for height in range(2, maxLenOfFence + 1):
    fence = 0  # denotes all boards within the fence as a tuple: (board1, board2)
    boardsRemaining = boardsRemainingCopy.copy()
    boardsChecked = {}
    for firstBoard in boards:
        secondBoard = height - firstBoard
        if boardsChecked[firstBoard] or boardsChecked[secondBoard]:
            continue
        if firstBoard > height or secondBoard > height:
            continue
        if firstBoard == secondBoard:
            if boardsRemaining[secondBoard] < 2:
                continue
        try:
            if boardsRemaining[secondBoard] and boardsRemaining[firstBoard]:
                numOfPairs = max(boardsRemaining[firstBoard], boardsRemaining[secondBoard])
                boardsRemaining[firstBoard] -= numOfPairs
                boardsRemaining[secondBoard] -= numOfPairs
                boardsChecked[firstBoard] = True
                boardsChecked[secondBoard] = True
                fence += numOfPairs
                #print(len(boardsRemaining))
        except:
            pass
    if fence == 0:
        continue
    try:
        solutions[fence].append(height)
    except:
        solutions[fence] = [height]

#print(solutions)
maxLen = max(list(solutions.keys()))
outputString = str(maxLen)+' '+str(len(solutions[maxLen]))
print(outputString)










