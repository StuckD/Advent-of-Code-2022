def areaToString(a):
    s = ""
    for c in a:
        s += str(c) + ","
    return(s)

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

    ## Doesnt work :()
    # overlaps = 0
    # pairs = map(lambda x: x.split(","), inputs)
    # pairs = map(lambda x: map(lambda y: y.replace("\n", ""), x), pairs)

    # for p in pairs:
    #     p = list(p)
    #     old_pair_start = 0
    #     for i in enumerate(p):
    #         if i[0] == old_pair_start:
    #             continue

    #         old_pair_start+= 2
    #         first_area = list(p)[i[0]-1].split("-")
    #         second_area = list(p)[i[0]].split("-")

    #         first_area_string = areaToString(list(range(int(first_area[0]), int(first_area[1])+1)))
    #         second_area_string = areaToString(list(range(int(second_area[0]), int(second_area[1])+1)))

    #         if first_area_string.__contains__(second_area_string) or second_area_string.__contains__(first_area_string):
    #             overlaps+=1
    return(matches)