from dataclasses import dataclass

@dataclass
class Position:
    x:int = 0
    y:int = 0

    def __iadd__(self,other):
        self.x+=other.x
        self.y+=other.y
        return self

def checkSlope(areaMap,slope):#Check the amount of trees in your trajectory descending areaMap with given slope.
    pos = Position(0,0)
    trees = 0
    while pos.x < len(areaMap):
        pos.y%= len(areaMap[pos.x])
        if areaMap[pos.x][pos.y]=='#':
            trees+=1
        pos+= slope
    return trees

def part1(areaMap):#checkSlope with slope (1,3)
    return checkSlope(areaMap,Position(1,3))

def part2(areaMap):#checks trees encountered for each of the requested slopes and returns its product
    slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    res = 1
    for x,y in slopes:
        res*=checkSlope(areaMap,Position(x,y))
    return res

with open('3.in') as inputFile:
    inputLines = inputFile.read().splitlines()
    print('Solutions:')
    print('Trees encountered with slope 1,3:', part1(inputLines))
    print('Product of Trees encountered with each slope:', part2(inputLines))
