from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass
class Passport:
    requiredFields:ClassVar[set[str]] = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fieldBounds:ClassVar[dict[str,tuple]] = {'byr':(1920,2002), 'iyr':(2010,2020), 'eyr':(2020,2030), 'cm':(150,193), 'in':(59,76)}
    fieldFormat:ClassVar[dict[str,str]] = {'byr':'\d{4}', 'iyr':'\d{4}', 'eyr':'\d{4}', 'hgt':'\d+(cm|in)', 'hcl':'#[0-9a-f]{6}', 'ecl':'amb|blu|brn|gry|grn|hzl|oth', 'pid':'\d{9}'} 
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    #hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #pid (Passport ID) - a nine-digit number, including leading zeroes.

    fields:dict

    def __init__(self,desc):
        self.fields = {}
        for field in re.split('[ \n]',desc):
            (key,value) = field.split(':')
            if key in Passport.requiredFields:
                self.fields[key]=value

    def checkBounds(self,field):
        if field not in (Passport.fieldBounds | {'hgt':''}):
            return True
        if field == 'hgt':
            (boundsKey,boundedValue) = (self.fields[field][-2:],int(self.fields[field][:-2]))
        else:
            (boundsKey,boundedValue) = (field,int(self.fields[field]))
        (lo,hi) = Passport.fieldBounds[boundsKey]
        return lo <= boundedValue <= hi

    def valid(self):
        for field in Passport.requiredFields:
            if not (
                    field in self.fields and
                    re.fullmatch(Passport.fieldFormat[field],self.fields[field]) is not None and
                    self.checkBounds(field)
                    ):
                return False
        return True

def part1(inputBatch):
    validPassports=0
    for passportDesc in inputBatch.split('\n\n'):
        act = Passport(passportDesc)
        if len(act.fields) == 7:
            validPassports+=1
    return validPassports

def part2(inputBatch):
    validPassports=0
    for passportDesc in inputBatch.split('\n\n'):
        act = Passport(passportDesc)
        if len(act.fields) == 7 and act.valid():
            validPassports+=1
    return validPassports

with open('4.in') as inputFile:
    inputBatch = inputFile.read()
    inputBatch = inputBatch.rstrip('\n')#last newline breaks the pattern and fucks up parsing
    print('Solutions:')
    print('Passports with all the fields:', part1(inputBatch))
    print('Passports with valid values', part2(inputBatch))
