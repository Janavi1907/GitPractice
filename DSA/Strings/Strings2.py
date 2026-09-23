#Task 1
word = "Programming"
count=0
for i in word:
    count+=1
print("Total characters in word:",count)

#Task 2
word = "banana"
count_a=0
for i in word:
    if i=="a":
        count_a+=1
print("Number of a's in word:",count_a)

#Task 3
word = "DataScience"
count_vowel=0
for i in word:
    if i in "aeiouAEIOU":
        count_vowel+=1
print("Number of vowels in word:",count_vowel)

#⭐ Mini Challenge
word = "HelloWorld"
Count_H=0
Count_e=0
Count_l=0
Count_o=0
for i in word:
    if i=="H":
        Count_H+=1
    elif i=="e":
        Count_e+=1
    elif i=="l":
        Count_l+=1
    elif i=="o":
        Count_o+=1
print("Number of H's in word:",Count_H)
print("Number of e's in word:",Count_e)
print("Number of l's in word:",Count_l)
print("Number of o's in word:",Count_o)


