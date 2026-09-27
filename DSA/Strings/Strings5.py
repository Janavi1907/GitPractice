#Task 1
word = "computer"
reverse=""
for i in word:
    reverse=i+reverse
print(reverse)

#Task 2
word = "racecar"
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

#Task 3
word = "engineering"
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#Task 4
word1 = "triangle"
word2 = "integral"
frequency1={}
frequency2={}
for i in word1:
    if i in frequency1:
        frequency1[i]+=1
    else:
        frequency1[i]=1
for i in word2:
    if i in frequency2:
        frequency2[i]+=1
    else:
        frequency2[i]=1
if frequency1==frequency2:
    print("Anagram")
else:
    print("Not Anagram")

#task 5
word = "programming"
char = "g"
for i in range(len(word)):
    if char==word[i]:
        print("First occurrence of",char,"is at index",i)
        break