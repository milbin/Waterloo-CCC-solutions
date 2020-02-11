import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
sequenceInput = input[1].split(' ')
sequence = []
for i in sequenceInput:
    sequence.append(int(i))
sequence = sorted(sequence)
sequenceOutput = ''
for i in sequence:
    sequenceOutput += str(i)+' '

print(sequenceOutput)


