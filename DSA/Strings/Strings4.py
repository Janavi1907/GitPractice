#Task 1
word = "banana"
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#Task 2
word = "Programming"
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#Task 3
word = "banana"
max_frequency=0
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
    if frequency[i]>max_frequency:
        max_frequency=frequency[i]
        max_char=i
print("Most Frequent Character:",max_char)
print("Frequency:",max_frequency)

#Task 4
word = "mississippi"
max_frequency=0
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
    if frequency[i]>max_frequency:
        max_frequency=frequency[i]
        max_char=i
print(frequency)
print("Most Frequent Character:",max_char)
print("Frequency:",max_frequency)

#Task 5
word = "programming"
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for i in frequency:
    if frequency[i]>1:
        print(i)

#Task 6
word = "programming"
word_new=""
for i in word:
    if i not in word_new:
        word_new+=i
print(word_new)

#Task 7
word1 = "listen"
word2 = "silent"
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


#Final Challenge
word = "datascience"
max_frequency=0
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
    if frequency[i]>max_frequency:
        max_frequency=frequency[i]
        max_char=i    
print("Most Frequent Character:",max_char)
print("Frequency:",max_frequency)
print(frequency)
for i in frequency:
    if frequency[i]>1:
        print(i)
no_unique=0
print("Number of unique characters:",len(frequency))