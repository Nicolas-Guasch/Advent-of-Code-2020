import re
seatIndex = {'F':0,'B':1,'L':0,'R':1}


def part1(inputLines):
    highestSeatID=0
    for seat in inputLines:
        seatID=0
        for ch in seat:
            seatID=2*seatID+seatIndex[ch]
        highestSeatID = max(highestSeatID,seatID)
    return highestSeatID

def part2(inputLines):#originally I found the missing value by hand
    ids=[]
    for seat in inputLines:
        seatID=0
        for ch in seat:
            seatID=2*seatID+seatIndex[ch]
        ids.append(seatID)
    ids.sort()
    for i in range(0,len(ids)-1):
        if ids[i+1]-ids[i]>1:
            return ids[i]+1

with open('5.in') as inputFile:
    inputLines = inputFile.read().splitlines()
    print('Solutions:')
    print('highest seat ID:', part1(inputLines))
    print('missing seat:', part2(inputLines))
