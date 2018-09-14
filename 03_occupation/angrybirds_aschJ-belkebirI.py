# Team Angry Birds - Jared Asch, Imad Belkebir
# SoftDev1 pd7
# K#06 -- StI/O: Divine your Destiny!
# 2018-09-13

from random import random

def readlines():
    f = open('occupations.csv', 'r')
    text = f.read().strip().split('\n')
    f.close()
    return text[1:][:-1]

def linesToDict(lines):
    info_dict = {}
    for line in lines:
        if line[0] is '\"':
            end = line[1:].find('\"')
            job = line[1:end]
            info_dict[job] = float(line[end+3:])
        else:
            job = line.split(',')[0]
            info_dict[job] = float(line.split(',')[1])
    return info_dict

def pickOccupation(occupations):
    percents = list(occupations.values())
    occs = list(occupations.keys())
    rand = random() * 99.8
    percentTot = percents[0];
    index = 0;
    while(percentTot < rand):
        index += 1
        percentTot += percents[index]
    return (occs[index])

def randomOccupation():
    return pickOccupation(linesToDict(readlines()))

print(randomOccupation())

