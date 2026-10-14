#Min element in an array
arr = [7, 4, 9, 5, 1]
min_index=0
for i in range (len(arr)):
    if arr[i]<arr[min_index]:
        min_index=i
print(min_index)
print(arr[min_index])

#Selection sort(ascending order)
arr = [7, 4, 9, 2, 5]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)

#Selection sort(descending order)
arr = [3, 8, 1, 6, 4]
for i in range (len(arr)):
    max_index=i
    for j in range(i+1,len(arr)):
        if arr[j]>arr[max_index]:
            max_index=j
    arr[i],arr[max_index]=arr[max_index],arr[i]
print(arr)

#Swap_count
arr = [1, 2, 3, 4]
swap_count=0
for i in range (len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swap_count += 1
print(arr)
print(swap_count)