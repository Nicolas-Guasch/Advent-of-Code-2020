import re;

#amount of valid passwords in database. 
#Password is valid if number of times the specified letter appears is between the bounds specified. 
#Format: 'lowerbound-upperbound letter: password'
def part1(database):
    validPasswords=0
    for entry in database:
        (lowerbound,upperbound, (letter,*_), password) = re.split('-| ',entry)
        if int(lowerbound) <= password.count(letter) <= int(upperbound):
            validPasswords+=1
    return validPasswords


#amount of valid passwords in database. 
#Password is valid if letter appears exactly once on the two specified 1-based positions. 
#Format: 'firstPos-secondPos letter: password'
def part2(database):
    validPasswords=0
    for entry in database:
        (firstPos,secondPos, (letter,*_), password) = re.split('-| ',entry)
        (i,j) = (int(firstPos)-1,int(secondPos)-1)
        if [password[i],password[j]].count(letter) == 1:
            validPasswords+=1
    return validPasswords

with open('2.in') as inputFile:
    inputLines = inputFile.read().splitlines()
    print('Solutions:')
    print('ValidPasswords:', part1(inputLines))
    print('ValidPasswords:', part2(inputLines))
