#Task 1
def product_digits(n):
    if n==0:
        return 1
    return n%10 *product_digits(n//10)
print("Product of digits:",product_digits(234))

#task 2
def sum_natural(n):
    if n==0:
        return 0
    return n + sum_natural(n-1)
print("Sum of Natural Numbers:",sum_natural(5))

#task 3
def reverse_string(s):
    if len(s)==0:
        return s
    return s[-1]+reverse_string(s[:-1])
print(reverse_string("hello"))

#task 4
def is_palindrome(s):
    if len(s)<=1:
        return True 
    if s[0]==s[-1]:
        return is_palindrome(s[1:-1])
    return False
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("level"))  # True

#task 5
def count_digits(n):
    if n<10:
        return 1
    return 1+count_digits(n//10)
print ("Number of digits:",count_digits(1234))

#task 6
def sum_digits(n):
    if n==0:
        return 0
    return n%10 + sum_digits(n//10)
print("Sum of Digits:",sum_digits(1234))

#task 7
def product_digits(n):
    if n<10:
        return n
    return n%10 *product_digits(n//10)
print("product of Digits:",product_digits(105))
    
    