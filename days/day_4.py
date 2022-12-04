def solve(inputs):
    matches = 0
    for line in inputs:
        line = line.replace('\n', '')
        linesplit = line.split(',')
        a = linesplit[0].split('-')
        b = linesplit[1].split('-')
        if int(a[0]) == int(b[0]) and int(a[1]) == int(b[1]):
            matches += 1
        elif int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
            matches += 1
        elif int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1]):
            matches += 1

    #part 2
    intersections = 0
    for line in inputs:
        line = line.replace('\n', '')
        linesplit = line.split(',')
        a = linesplit[0].split('-')
        b = linesplit[1].split('-')
        a = set(range(int(a[0]), int(a[1])+1))
        b = set(range(int(b[0]), int(b[1])+1))
        if a.intersection(b):
            intersections+= 1
    return([matches, intersections])