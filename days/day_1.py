import os

def solve(inputs):
    elves_rations = [[]]
    current_elve = 0
    if not inputs:
        path = (os.path.abspath(__file__).replace("/days/day_1.py", "/raw_inputs/raw_input_1.text"))
        file = open(path, "r")
    elves = inputs or file.readlines()

    for elve in elves:
        if elve == "\n":
            current_elve+=1
            elves_rations.append([])
        else:
            elve.replace("\n", "")
            elves_rations[current_elve].append(int(elve))

    total_rations = []
    for rations in elves_rations:
        sum_ration = 0
        for ration in rations:
            sum_ration = sum_ration + ration
        total_rations.append(sum_ration)

    largest_ration = 0
    total_rations.sort()
    largest_ration = total_rations[len(total_rations) -1]

    ## part 2
    sum_top_ration = total_rations[len(total_rations) -1] + total_rations[len(total_rations) -2] + total_rations[len(total_rations) -3]

    return([largest_ration, sum_top_ration])