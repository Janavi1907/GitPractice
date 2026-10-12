#Selection sorting 
arr = [7, 4, 9, 5, 1]
min_index=0
for i in range (len(arr)):
    if arr[i]<arr[min_index]:
        min_index=i
print(min_index)
print(arr[min_index])