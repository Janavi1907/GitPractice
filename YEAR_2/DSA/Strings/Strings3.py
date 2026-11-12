#Task 1
word = "Python"
print(word[::-1])

#Task 2
word = "DataScience"
reverse=""
for i in word:
    reverse=i+reverse
print(reverse)

#Task 3
word = "madam"
palindrome=True
for i in range(len(word)):
    if word[i]!=word[(len(word)-1)-i]:
        palindrome=False
        break
if palindrome:
    print("The string is a palindrome")
else:
    print("The string is NOT a palindrome")

#Task 4
word = "level"
left=0
right=len(word)-1
while left<right:
    if word[left]!=word[right]:
        print("The string is NOT a palindrome")
        break
    left+=1
    right-=1
else:
    print("The string is a palindrome")
