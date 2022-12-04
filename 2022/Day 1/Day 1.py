elves = []


with open('Day 1\data.txt') as opened:
    data = [opened.read()]

data = '\n'.join(data).split('\n\n')

for elf in data:
    elf_sum = 0
    for x in elf.split('\n'):
        elf_sum += int(x)
    elves.append(elf_sum)
elves = sorted(elves, reverse=True)

print(max(elves))
print(sum(elves[0:3]))