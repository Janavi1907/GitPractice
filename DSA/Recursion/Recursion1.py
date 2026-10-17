#Task 1
def count_down(n):
    if n==0:
        return
    print(n)
    count_down(n-1)
count_down(5)


#Task 2
def count_up(n):
    if n==5:
        print(n)
        return
    print(n)
    count_up(n+1)
count_up(1)

#Task 3
def sum_numbers(n):
    if n==0:
        return 0
    return n + sum_numbers(n-1)
print("Sum of Natural Numbers: ",sum_numbers(4))

#Task 4
def power(base,exp):
    if exp==0:
        return 1
    return base * power(base,exp-1)
print("Power of a Number: ",power(2,4))

#Task 5
def sum_digits(n):
    if n==0:
        return 0
    return n%10 + sum_digits(n//10)
print("Sum of Digits: ",sum_digits(1234))

#Task 6
def sum_even(n):
    if n==0:
        return 0
    if n%2==0:
        return n + sum_even(n-1)
    else:
        return sum_even(n-1)
print("Sum of Even Numbers: ",sum_even(6))