import os
import random
import time




def generateData():
    N = random.choice(range(2, 101))
    returnString = str(N)+'\n'
    for i in range(N):
        returnString += str(random.choice(range(1, 2000)))+' '
    return returnString[:-1]



for i in range(10):
    with open('input.txt', 'w') as file:
        data = generateData()
        file.write(data)

    os.system('python "CCC 2017"/Q3.py < input.txt')
    print('--------------------------------------------------------------')
    time.sleep(2)
