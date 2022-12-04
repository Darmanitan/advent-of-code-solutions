sum = 0

with open('Day 2/data.txt') as opened:
    data = opened.read().split('\n')

for scenario in data:
    #--- ROCK ---#
    if scenario[0] == "A" and scenario[2] == "X":
        sum += 0 + 3
    if scenario[0] == "A" and scenario[2] == "Y":
        sum += 3 + 1
    if scenario[0] == "A" and scenario[2] == "Z":
        sum += 6 + 2
    #--- PAPER ---#
    if scenario[0] == "B" and scenario[2] == "X":
        sum += 0 + 1
    if scenario[0] == "B" and scenario[2] == "Y":
        sum += 3 + 2
    if scenario[0] == "B" and scenario[2] == "Z":
        sum += 6 + 3
    #--- SCISSORS ---#
    if scenario[0] == "C" and scenario[2] == "X":
        sum += 0 + 2
    if scenario[0] == "C" and scenario[2] == "Y":
        sum += 3 + 3
    if scenario[0] == "C" and scenario[2] == "Z":
        sum += 6 + 1

print(sum)