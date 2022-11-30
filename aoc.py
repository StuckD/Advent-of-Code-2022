import os
import sys

#import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)) + "/days")
sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)) + "/inputs")
day_modules = []
input_modules = []
day_list = os.listdir("days")
input_list = os.listdir("inputs")
day_list.remove("__pycache__")
input_list.remove("__pycache__")
for m in day_list:
    day_modules.append(__import__(m.replace(".py", "")))
for i in input_list:
    input_modules.append(__import__("inputs_" + m.replace(".py", "")).input)

argument_list = sys.argv[1:]
if argument_list[1:]:
    argument_list = [argument_list[0],argument_list[1:]]
else:
    argument_list.append(input_modules[0])

#solve current day
result = day_modules[int(argument_list[0])-1].solve(argument_list[1])
print(result)