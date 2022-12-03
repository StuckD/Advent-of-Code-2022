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

        # part 2
        groups = [[]]
        current_group = 0
        for i in inputs:
            rucksack = i.replace("\n", "")
            if len(groups[current_group]) == 3:
                current_group+=1
                groups.append([])
            groups[current_group].append(rucksack)

        total_sum = 0
        for group in groups:
            group_badge = ""
            for badge in group[0]:
                if group[1].__contains__(badge) and group[2].__contains__(badge) and badge != group_badge:
                    group_badge = badge

            total_sum+= priority_list.rfind(group_badge)+1
        return([result, total_sum])