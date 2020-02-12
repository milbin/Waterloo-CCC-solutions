import sys
input = sys.stdin.read().splitlines()
N = int(input[0])
readings = []
for reading in input[1:]:
    readings.append(int(reading))

readingFreq = {}
for reading in readings:
    #if not readingFreq.get(reading, False):
    readingFreq[reading] = readings.count(reading)

mostFrequentList = []  # contains actual values of the readings, not their freq
secondMostFrequentList = []
mostFrequent = 0
secondMostFrequent = 0
readings = sorted(readings)
for reading in readings:
    freqOfReading = readingFreq[reading]
    if freqOfReading > mostFrequent:
        secondMostFrequentList = mostFrequentList.copy()
        secondMostFrequent = int(mostFrequent)
        mostFrequentList.clear()
        mostFrequentList.append(reading)
        mostFrequent = freqOfReading
    elif freqOfReading == mostFrequent:
        if reading not in mostFrequentList:
            mostFrequentList.append(reading)
    elif freqOfReading > secondMostFrequent:
        secondMostFrequentList.clear()
        secondMostFrequentList.append(reading)
        secondMostFrequent = freqOfReading
    elif freqOfReading == secondMostFrequent:
        if reading not in secondMostFrequentList:
            secondMostFrequentList.append(reading)

if len(mostFrequentList) == 0:
    print(-1)


if len(mostFrequentList) > 1:
    print(abs(max(mostFrequentList) - min(mostFrequentList)))
elif len(secondMostFrequentList) == 0:
    print(mostFrequentList[0])
elif abs(mostFrequentList[0] - min(secondMostFrequentList)) > abs(mostFrequentList[0] - max(secondMostFrequentList)):
    print(abs(mostFrequentList[0] - min(secondMostFrequentList)))
else:
    print(abs(mostFrequentList[0] - max(secondMostFrequentList)))
