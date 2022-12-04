with open('2022\Day 3\data.txt') as opened:
    data = opened.read().split("\n")

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def common_data(list):
    for x in list[0]:
        for y in list[1]:
            for z in list[2]:
                if x==y==z:
                    return priorities.index(x) + 1
    return None

priority_sum = 0
lines = []

for i in range(0, len(data), 3): # split strings into 3
    lines.append(data[i:i+3])

for list in lines:
    priority_sum += common_data(list)
    print(priority_sum)