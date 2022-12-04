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
    return(matches)