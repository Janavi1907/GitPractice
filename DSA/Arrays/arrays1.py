# Task 1
numbers = [10, 20, 30, 40, 50]
print("first element:",numbers[0])
print("third element:",numbers[2])
print("last element:",numbers[-1])
print("length:",len(numbers))

# Task 2
numbers[2]=100
print(numbers)

# Task 3
for items in numbers:
    print(items)

# Task 4
total=0
for i in numbers :
    total=total+i
print("Sum:",total)

# Task 5
numbers1 = [12, 45, 7, 89, 23]
max_no=numbers1[0]
for a in numbers1:
    if a>max_no:
        max_no=a
print("Greatest number:",max_no)

# Task 6
min_no=numbers1[0]
for num in numbers1:
    if num<min_no:
        min_no=num
print("Smallest number:",min_no)

#DSA 1
arr = [4, 9, 2, 7, 9, 3, 9, 1]
# 1
max_num = arr[0]
for i in arr:
    if i > max_num:
        max_num = i
print("Greatest number in arr:", max_num)
# 2
min_num = arr[0]
for i in arr:
    if i < min_num:
        min_num = i
print("Smallest number in arr:", min_num)
# 3
total_arr=0
for ele in arr:
    total_arr=total_arr+ele
print("Sum of all elements:",total_arr)
#4
print("number of elements:",len(arr))
#5
count_9=0
for num in arr:
    if num==9:
        count_9+=1
print("Count of 9 in arr:",count_9)