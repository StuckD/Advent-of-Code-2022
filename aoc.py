import os
import sys

#import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)) + "/days")
sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)) + "/inputs")
day_modules = []
input_modules = []
day_list = os.listdir("days")
input_list = os.listdir("inputs")
day_list.sort()
input_list.sort()
day_list.pop(0)
input_list.pop(0)
for m in day_list:
    day_modules.append(__import__(m.replace(".py", "")))
for i in input_list:
    i = i.replace(".py", "")
    input_modules.append(__import__(i))
    if not input_modules[-1].inputs:
        current_day = i[-1]
        path = os.path.abspath(__file__).replace("/aoc.py", "/raw_inputs/raw_%s.text" %(i)).replace("_day", "")
        file = open(path, "r")
        inputs = file.readlines()
        file.close()
        path = (os.path.abspath(__file__).replace("/aoc.py", "/inputs/%s.py" %(i)))
        file = open(path, "a")
        file.truncate(0)
        file.write("inputs = %s" %inputs)
        file.close()
    input_modules[-1].inputs = input_modules[-1].inputs or inputs


argument_list = sys.argv[1:]
if argument_list[1:]:
    argument_list = [argument_list[0],argument_list[1:]]
else:
    argument_list.append(input_modules[int(argument_list[0])-1].inputs)

#solve current day
result = day_modules[int(argument_list[0])-1].solve(argument_list[1])
print(result)