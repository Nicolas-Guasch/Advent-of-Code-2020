year = 2020
def part1(reportFile): #Given a list of integers output the product of the pair that sums 2020
    report = set()

    for expense in reportFile:
        val = int(expense)
        if year-val in report:
            return val*(year-val)
        report.add(val)

def part2(reportFile): #Given a list of integers output the product of the 3-tuple that sums 2020
    year = 2020
    report = set()
    pairSums = dict()

    for expense in reportFile:
        val = int(expense)
        if year-val in pairSums:
            return val*pairSums[year-val]
        pairSums|= dict((val+x,val*x) for x in report)
        report.add(val)

with open('1.in') as inputFile:
    inputLines = inputFile.read().splitlines()
    print('Solutions\n')
    print('Pair: '+ str(part1(inputLines)))
    print('Product: ' + str(part2(inputLines)))
