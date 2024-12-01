inputArray = []
distances = []
left = []
right = []

# parse input
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        inputArray.append(line.strip().split())

# append to separate lists
for i in range(len(inputArray)):
    left.append(inputArray[i][0])
for j in range(len(inputArray)):
    right.append(inputArray[j][1])

def bubbleSort(arr):
    for n in range(len(arr) - 1, 0, -1):

        swapped = False  
        
        for i in range(n):
            if arr[i] > arr[i + 1]:
                
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                swapped = True
        
        if not swapped:
            break

bubbleSort(left)
bubbleSort(right)

for i in range(len(left)):
    if left[i] > right[i]:
        distances.append(int(left[i]) - int(right[i]))
    else:
        distances.append(int(right[i]) - int(left[i]))

print(sum(distances))