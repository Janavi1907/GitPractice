#INSERTION SORTING

#Task1
from itertools import count


arr = [6, 2, 5, 3, 1]
#[6| 2, 5, 3, 1]
#[2, 6| 5, 3, 1]
#[2,5, 6| 3, 1]
#[2, 3, 5, 6| 1]
#[1, 2, 3, 5, 6]

#Task 2 in ascending order
arr = [6, 2, 5, 3, 1]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(arr)

#Task 3 in descending order
arr = [4, 7, 2, 9, 1, 5]
for i in range(1,len(arr)):
    key =arr[i]
    j=i-1
    while j>=0 and arr[j]<key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)

#Task 4(Bubble Sort)
arr = [5, 1, 4, 2, 8]
pass_num=0
pass_count=0
while True:
    swapped=False
    for i in range(len(arr)-1-pass_num):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped=True
            pass_count+=1
    pass_num+=1
    if not swapped:
        break
print(arr)
print("Total swaps:",pass_count)