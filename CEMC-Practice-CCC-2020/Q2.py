import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
team1 = input[1]
team2 = input[2]
runs1 = []
runs2 = []
for run in team1.split(' '):
    runs1.append(int(run))
for run in team2.split(' '):
    runs2.append(int(run))

K = 0
team1Total = 0
team2Total = 0
for dayNumber in range(len(runs1)):
    team1Total += runs1[dayNumber]
    team2Total += runs2[dayNumber]
    if team1Total == team2Total:
        K = abs(dayNumber+1)


print(K)

