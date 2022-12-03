import os
def solve(inputs):
        if not inputs:
            path = (os.path.abspath(__file__).replace("/days/day_3.py", "/raw_inputs/raw_input_3.text"))
            file = open(path, "r")
            inputs = file.readlines()
            file.close()
            path = (os.path.abspath(__file__).replace("/days/day_3.py", "/inputs/inputs_day_3.py"))
            file = open(path, "a")
            file.truncate(0)
            file.write("inputs = %s" %inputs)
            file.close()

        rucksacks = []
        for j in inputs:
            i = j.replace("\n", "")
            rucksacks.append([i[0:(len(i)//2)], i[(len(i)//2):]])

        priority_list ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = 0

        for compartments in rucksacks:
            old_item = ""
            for item in compartments[0]:
                if compartments[1].__contains__(item) and not item == old_item:
                    result+= priority_list.rfind(item)+1
                    old_item = item
        return(result)