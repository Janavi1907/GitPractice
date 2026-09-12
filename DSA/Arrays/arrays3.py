#Task 1
arr = [10, 25, 30, 45, 50]
index_find=int(input("Enter element in arr: "))
index=0
for i in arr:
    if i==index_find:
        print("Element is present in arr at index:",index)
        break
    index+=1
else:
    print("Element is not present in arr")

#Task 2
arr1= [4, -2, 7, -9, 0, 5, -1, 8]
positive_count=0
negative_count=0
zero_count=0
for i in arr1:
    if i==0:
        zero_count+=1
    elif i>0:
        positive_count+=1
    else:
        negative_count+=1
print("Number of positive numbers in arr1:", positive_count)
print("Number of negative numbers in arr1:", negative_count)
print("Number of zeros in arr1:", zero_count)

#task 3
arr2 = [12, 45, 7, 89, 23, 56]
second_largest = arr2[0]
largest = arr2[0]
for i in arr2:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Second largest number in arr2:", second_largest)

#task 4
arr3 = [1, 2, 3, 4, 5]
reversed_arr3 = []
for i in range(len(arr3), 0, -1):
    reversed_arr3.append(arr3[i-1])
print("Reversed array:", reversed_arr3)

#DSA
arr4 = [5, 2, 8, 2, 9, 1, 5, 8, 3]
#1
maximum=arr4[0]
for i in arr4:
    if i>maximum:
        maximum=i
print("Greatest Number: ",maximum)
#2
minimum=arr4[0]
for i in arr4:
    if i<minimum:
        minimum=i
print("Smallest Number: ",minimum)
#3
second_largest_arr4 = arr4[0]
for i in arr4:
    if i > second_largest_arr4 and i != maximum:
        second_largest_arr4 = i
print("Second largest number in arr4:", second_largest_arr4)
#4
even_count=0
for num in arr4:
    if num%2==0:
        even_count+=1
print("Count of even numbers in arr4:", even_count)
#5
odd_count=0
for num in arr4:
    if num%2!=0:
        odd_count+=1
print("Count of odd numbers in arr4:", odd_count)
#6
positive_count_arr4=0
for num in arr4:
    if num>0:
        positive_count_arr4+=1
print("Count of positive numbers in arr4:", positive_count_arr4)
#7
count_of_5=0
for num in arr4:
    if num==5:
        count_of_5+=1
print("Count of 5 in arr4:", count_of_5)
#8
index_of_8=-1
for i in range(len(arr4)):
    if arr4[i]==8:
        index_of_8=i
        break
print("First Index of 8 in arr4:", index_of_8)
#9
duplicate_found=False
for i in range(len(arr4)):
    for j in range(i+1, len(arr4)):
        if arr4[i]==arr4[j]:
            duplicate_found=True
            break
if duplicate_found:
    print("Duplicate elements found in arr4.")
else:
    print("No duplicate elements found in arr4.")
#10
duplicate_elements=[]
for i in range(len(arr4)):
    for j in range(i+1, len(arr4)):
        if arr4[i]==arr4[j] and arr4[i] not in duplicate_elements:
            duplicate_elements.append(arr4[i])
print("Duplicate elements: ",duplicate_elements)