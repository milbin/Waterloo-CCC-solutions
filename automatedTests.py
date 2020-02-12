import os
import random
import time




def generateData(i):
    #num = ''
    #if i < 10:
    #    num += '0'+str(i)
    #else:
    num = str(i)
    with open(f'inputs/s3.{num}.in', 'r') as txtFile:
        return txtFile.read()



for i in range(1, 28):
    with open('input.txt', 'w') as file:
        data = generateData(i)
        file.write(data)
    result = os.system('python "CEMC-Practice-CCC-2020"/Q3.py < input.txt')
    print(result)
    print(f'--------------------- TEST: {i} -----------------------------------------')

    time.sleep(2)
