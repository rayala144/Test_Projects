print("Enter array 1")
arr1 = [input() for i in range(4)]
print("Enter array 2")
arr2 = [input() for i in range(4)]
indexes = []
for i in range(4):
    if arr1[i] not in arr2:
        indexes.append('NA')
    for j in range(4):
        if arr1[i] == arr2[j]:
            indexes.append(j)

for i in range(4):
    print(f'{arr1[i]} - {indexes[i]}')
