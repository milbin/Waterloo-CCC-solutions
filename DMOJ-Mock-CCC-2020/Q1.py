import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
player1 = input[1].split(' ')
player2 = input[2].split(' ')

numberOfWars = 0
warOngoing = False
for i in range(N):
    if warOngoing and player1[i] != player2[i]:
        warOngoing = False
        continue
    if player1[i] == player2[i] and not warOngoing:
        warOngoing = True
        numberOfWars += 1
print(numberOfWars)


