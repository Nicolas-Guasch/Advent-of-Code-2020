import re
import string

def strToBitset(answer):
    bitset=0
    for c in answer:
        bitset|= 1<<(ord(c)-ord('a'))
    return bitset

def part1(passengerGroups):
    count = 0
    for group in passengerGroups:
        bitset = strToBitset(group.replace('\n',''))
        count+= bin(bitset).count('1')
    return count

def part2(passengerGroups):
    count = 0
    for group in passengerGroups:
        bitset = strToBitset(string.ascii_lowercase)
        for passenger in group.splitlines():
            bitset &= strToBitset(passenger)
        count+= bin(bitset).count('1')
    return count

with open('6.in') as inputFile:
    passengerGroups = re.split('\n\n',inputFile.read().rstrip('\n'))
    print('Amount of answers anyone in a group replied positively:',part1(passengerGroups))
    print('Amount of answers everyone in a group replied positively:',part2(passengerGroups))
