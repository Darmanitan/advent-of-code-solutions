import re

with open('2022\Day 4\dd.txt') as opened:
    data = opened.read().split("\n")

pairs = []

for x in data: 
    pairs.append(re.split(",|-", x)) # append values to a nested list, values seperated

global overlap_count
overlap_count = 0

def check_for_overlap(list):
    print(list)
    if list[0][0] < list[0][2] and list[0][1] > list[0][3]:
        return overlap_count + 1
    elif list[0][2] < list[0][0] and list[0][1] > list[0][4]:
        return overlap_count + 1
    else:
        return 0

for x in pairs:
    print(check_for_overlap(x))