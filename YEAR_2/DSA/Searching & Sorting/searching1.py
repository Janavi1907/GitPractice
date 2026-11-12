#Task 1
arr = [12, 45, 7, 23, 56, 19]
target = 23
for i in range(len(arr)):
    if arr[i]==target:
        print(target,"found at ",i)
        break
else:
    print(target,"not found in array")  

#Task 2
arr = [12, 45, 7, 23, 56, 19]
target = 100
for i in range(len(arr)):
    if arr[i]==target:
        print(target,"found at ",i)
        break
else:
    print(target,"not found in array")  

#Task 3
arr=[13,6,5,44,23,6744,34,65,]
element=6744
for i in range(len(arr)):
    if arr[i]==element:
        print(element,"found at ",i)
        break
else:
    print(element,"not found in array")  

