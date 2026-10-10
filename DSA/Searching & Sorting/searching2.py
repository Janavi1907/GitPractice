#Task 1
def linear_search(arr,element):
    for i in range(len(arr)):
        if arr[i]==element:
            return i
    return -1

arr = [8, 14, 3, 27, 19, 40]
print(linear_search(arr, 27))
print(linear_search(arr, 100))

#Task 2
arr = [9, 4, 7, 2, 6, 1]
while True:
    swapped=False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped=True
    if not swapped:
        break
print(arr)

#Task 3
arr = [9, 4, 7, 2, 6, 1]
swap_count=0
while True:
    swapped=False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped=True
            swap_count+=1
    if not swapped:
        break
print("Sorted array:",arr)
print("Total swaps:",swap_count)

#Task 4
arr = [7, 3, 5, 2, 1]
pass_num=0
swap_count=0
while True:
    swapped=False
    for i in range(len(arr)-1-pass_num):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped=True
            swap_count+=1
    pass_num+=1
    if not swapped:
      break
print("Sorted array:",arr)  
print("Total swaps:",swap_count)

