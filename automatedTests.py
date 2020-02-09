import os
import random
def generateBoard():
    N = random.choice(range(1, 50))
    board = []

    for i in range(N):
        row = []
        for x in range(N):
            row.append(random.choice(range(2)))
        board.append(row)

    boardString = (str(N) + '\n')
    for row in board:
        rowString = ''
        for i in row:
            rowString += (str(i) + ' ')
        boardString += (rowString[:-1] + '\n')
    #print(boardString)
    return boardString

for i in range(1000):
    with open('input.txt', 'w') as file:
        board = generateBoard()
        file.write(board)
    os.system('python DMOJ-Mock-CCC-2020/Q2.py < input.txt')
    print('--------------------------------------------------------------')