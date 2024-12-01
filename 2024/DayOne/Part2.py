inputArray = []
left = []
right = []
scores = []

# parse input
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        inputArray.append(line.strip().split())

# append to separate lists
for i in range(len(inputArray)):
    left.append(inputArray[i][0])
for j in range(len(inputArray)):
    right.append(inputArray[j][1])

# start loop
for x in range(len(left)):
    count = 0
    y = int(left[x]) 
    # for every element in right array
    for z in right:
        # if left == right (same number), increment count
        if y == int(z):
            count = count + 1
    if count != 0:
        # add score to scores
        scores.append(int(y * count))

print(sum(scores))