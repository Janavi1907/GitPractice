arr = [15, 3, 27, 8, 42, 19]

#Task 1
maximum=arr[0]
for num in arr:
    if num>maximum:
        maximum=num
print("Greatest number in arr:", maximum)

#Task 2
minimum=arr[0]
for num in arr: 
    if num<minimum:
        minimum=num
print("Smallest number in arr:", minimum)

#Task 3
arr1 = [10, 20, 30, 40, 50]
total = 0
for num in arr1:
    total += num
avg = total / len(arr1)
print("Average of all elements in arr1:", avg)

#Task 4
arr2 = [12, 7, 4, 9, 16, 3, 20, 11]
even_count=0
for num in arr2:
    if num%2==0:
        even_count+=1
print("Count of even numbers in arr2:", even_count)

#Task 5
greater10_count=0
for num in arr2:
    if num>10:
        greater10_count+=1  
print("Count of numbers greater than 10 in arr2:", greater10_count)

#Task 6
arr3 = [5, 12, 8, 20, 3, 15]
finding_num=int(input("Enter a number to find in arr3: "))
found=False
for num in arr3:
    if num==finding_num:
        found=True
        break
if found:
    print(f"{finding_num} is present in arr3.")
else:
    print(f"{finding_num} is not present in arr3.")

#DSA
arr4 = [7, 2, 9, 4, 2, 8, 2, 5]
#1
max_num = arr4[0]
for i in arr4:
    if i > max_num:
        max_num = i
print("Greatest number in arr4:", max_num)
#2
min_num = arr4[0]
for i in arr4:
    if i < min_num:
        min_num = i
print("Smallest number in arr4:", min_num)
#3
total_arr4=0
for i in arr4:
    total_arr4+=i
print("Sum of all elements in arr4:", total_arr4)
#4
average_arr4=total_arr4/len(arr4)
print("Average of all elements in arr4:", average_arr4)
#5
even_count_arr4=0
for i in arr4:
    if i%2==0:
        even_count_arr4+=1
print("Count of even numbers in arr4:", even_count_arr4)
#6
odd_count_arr4=0
for i in arr4:
    if i%2!=0:
        odd_count_arr4+=1
print("Count of odd numbers in arr4:", odd_count_arr4)
#7
count_2=0
for i in arr4:
    if i==2:
        count_2+=1
print("Count of 2 in arr4:", count_2)
#8
find_10=False
for i in arr4:
    if i==10:
        find_10=True
        break
if find_10:
    print("10 is present in arr4.")
else:   
    print("10 is not present in arr4.")
#Bonus
index_2=-1
for i in range(len(arr4)):
    if arr4[i]==2:
        index_2=i
        break
print("Index of 2 in arr4:", index_2)
