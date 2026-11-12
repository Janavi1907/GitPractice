#Bubble sorting
arr = [5, 2, 4, 1]
while True:
    swapped = False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped = True
    if not swapped:
        break
print(arr)