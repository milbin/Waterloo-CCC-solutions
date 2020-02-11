import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
boardsInput = input[1].split(' ')
boards = []
for board in boardsInput:
    boards.append(int(board))

boards = sorted(boards)
maxLenOfFence = int(boards[-1]*2)
solutions = {}
for height in range(2, maxLenOfFence + 1):
    fence = 0  # denotes all boards within the fence as a tuple: (board1, board2)
    boardsRemaining = boards.copy()
    for firstBoard in boards:
        secondBoard = height - firstBoard
        if firstBoard == secondBoard:
            if boardsRemaining.count(secondBoard) < 2:
                continue

        if secondBoard in boardsRemaining and firstBoard in boardsRemaining:
            fence += 1
            boardsRemaining.remove(firstBoard)
            boardsRemaining.remove(secondBoard)
            #print(len(boardsRemaining))
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










