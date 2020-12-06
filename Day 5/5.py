def part1(puzzleInput):
    highestSeatID=0
    puzzleInput = puzzleInput.translate(str.maketrans('FLBR','0011'))
    for seat in puzzleInput.splitlines():
        seatID=int(seat,2)
        highestSeatID = max(highestSeatID,seatID)
    return highestSeatID

def part2(puzzleInput):#originally I found the missing value by hand
    (lowestID,highestID) = (2**8-1,0)
    sumIDs=0
    puzzleInput = puzzleInput.translate(str.maketrans('FLBR','0011'))
    for seat in puzzleInput.splitlines():
        seatID=int(seat,2)
        sumIDs+=seatID
        highestID = max(highestID,seatID)
        lowestID = min(lowestID,seatID)
    return ((highestID*(highestID+1))//2 -
            (lowestID*(lowestID-1))//2     -
            sumIDs)
    #sum of elements in [lowest,highest] - sum of seen elements



with open('5.in') as inputFile:
    puzzleInput = inputFile.read()
    print('Solutions:')
    print('highest seat ID:', part1(puzzleInput))
    print('missing seat:', part2(puzzleInput))
