import os

def solve(inputs):
    if not inputs:
        path = (os.path.abspath(__file__).replace("/days/day_2.py", "/raw_inputs/raw_input_2.text"))
        file = open(path, "r")
        inputs = file.readlines()
        file.close()
        path = (os.path.abspath(__file__).replace("/days/day_2.py", "/inputs/inputs_day_2.py"))
        file = open(path, "a")
        file.truncate(0)
        file.write("inputs = %s" %inputs)
        file.close()

    strategy = []
    raw_strategy = inputs
    for i in raw_strategy:
        i.replace("/n", "")
        strategy.append([i[0], i[2]])

    total_score = 0
    for i in strategy:
        if i[1] == "X":
            total_score+=1
            if i[0] == "A":
                total_score+= 3
            elif i[0] == "B":
                total_score+= 0
            elif i[0] == "C":
                total_score+= 6
        if i[1] == "Y":
            total_score+=2
            if i[0] == "A":
                total_score+= 6
            elif i[0] == "B":
                total_score+= 3
            elif i[0] == "C":
                total_score+= 0
        if i[1] == "Z":
            total_score+=3
            if i[0] == "A":
                total_score+= 0
            elif i[0] == "B":
                total_score+= 6
            elif i[0] == "C":
                total_score+= 3
    # part 2
    win_score = 0
    for s in strategy:
        if s[1] == "X": #lose
            win_score +=0
            if s[0] == "A":
                win_score+=3
            elif s[0] == "B":
                win_score+=1
            elif s[0] == "C":
                win_score+=2
        elif s[1] == "Y": # draw
            win_score +=3
            if s[0] == "A":
                win_score+=1
            elif s[0] == "B":
                win_score+=2
            elif s[0] == "C":
                win_score+=3
        elif s[1] == "Z": #win
            win_score +=6
            if s[0] == "A":
                win_score+=2
            elif s[0] == "B":
                win_score+=3
            elif s[0] == "C":
                win_score+=1

    return([total_score, win_score])


