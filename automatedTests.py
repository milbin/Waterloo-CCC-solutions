import os
import random
import time




def generateData():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cStrings = ''
    qStrings = ''
    itterations = random.choice(range(1000))
    for i in range(itterations):
        cStrings += 'C '+str(random.choice(alphabet))+'\n'
        qStrings += 'Q '+str(random.choice(alphabet))+'\n'
    return 'chad '+str(itterations)+'\n'+cStrings+qStrings



for i in range(1):
    with open('input.txt', 'w') as file:
        data = generateData()
        file.write(data)

    os.system('python DMOJ-Mock-CCC-2020/Q3.py < input.txt')
    print('--------------------------------------------------------------')
    # time.sleep(2)
