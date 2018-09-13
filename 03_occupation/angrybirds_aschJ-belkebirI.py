def readlines():
    f = open('occupations.csv', 'r')
    text = f.read().strip().split('\n')
    f.close()
    return text

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
    return

print(linesToDict(readlines()[1:]))