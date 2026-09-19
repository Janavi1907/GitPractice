#Task 1
arr = [10, 20]
arr[0], arr[1] = arr[1], arr[0]
print(arr)

#Task 2
arr = [10, 20, 30, 40, 50]
left=0
right=len(arr)-1
print("Left index:",left)
print("Right index:",right)
print("Element at left index:",arr[left])
print("Element at right index:",arr[right])
left+=1
right-=1
print("Left index:",left)
print("Right index:",right)
print("Element at left index:",arr[left])
print("Element at right index:",arr[right])

#Task 3
arr = [1, 2, 3, 4, 5, 6,]
left=0
right=len(arr)-1
while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
print(arr)

#Mini Challenge
arr = [10, 20, 30, 40, 50, 60, 70]
left=0
right=len(arr)-1
while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
print(arr)

#Task 4
arr = [5, 10, 15, 20, 25]
left=0
right=len(arr)-1
while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
print(arr)

#Task 5
arr = [1, 2, 3, 2, 1]
left=0
right=len(arr)-1
is_palindrome=True
while left<right:
    if arr[left]!=arr[right]:
        is_palindrome=False
        break
    left+=1
    right-=1
if is_palindrome:
    print("The array is a palindrome")
else:
    print("The array is not a palindrome")
