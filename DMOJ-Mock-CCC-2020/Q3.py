import sys
input = sys.stdin.read().splitlines()
A = [input[0].split(' ')[0]]
operations = input[1:]

def copyOp(array, index, char):
    newString = array[index]
    newString += char
    array.append(newString)
    return array

def queryOp(array, subString):
    for lenOfSubstring in reversed(range(1, len(subString) + 1)):
        for i, string in enumerate(array):
            if string[:lenOfSubstring] == subString[:lenOfSubstring]:
                return i+1
    return -1


for op in operations:
    if op[0] == 'C':
        A = copyOp(A, int(op[2])-1, op[4])
    elif op[0] == 'Q':
        print(queryOp(A, op[2:]))



