sum = 0

with open('Day 2/data.txt') as opened:
    data = opened.read().split('\n')

for scenario in data:
    #--- ROCK ---#
    if scenario[0] == "A" and scenario[2] == "X":
        sum += 1 + 3
    if scenario[0] == "A" and scenario[2] == "Y":
        sum += 2 + 6
    if scenario[0] == "A" and scenario[2] == "Z":
        sum += 3 + 0
    #--- PAPER ---#
    if scenario[0] == "B" and scenario[2] == "X":
        sum += 1 + 0
    if scenario[0] == "B" and scenario[2] == "Y":
        sum += 2 + 3
    if scenario[0] == "B" and scenario[2] == "Z":
        sum += 3 + 6
    #--- SCISSORS ---#
    if scenario[0] == "C" and scenario[2] == "X":
        sum += 1 + 6
    if scenario[0] == "C" and scenario[2] == "Y":
        sum += 2 + 0
    if scenario[0] == "C" and scenario[2] == "Z":
        sum += 3 + 3
    
print(sum)