# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# from itertools import count
import collections
# age = input("enter your age:")

# try:
#     a = int(age)
#     ager = a/0
#     print("You Half Age is :", ager)
# except Exception as e:
#     print(e)

#
# a,b,c=1,2,2
# print(a,b)
# i=1010
# z=1010
# print(id(i),id(z))
# print(type(i))
#
# a="i am a learder"
# print(a.count("v"))

# class Cars:
#     def __init__(self, m, p):
#         self.model = m
#         self.price = p
#
#
# Audi = Cars("R8", 54545454)
#
# print(Audi.model)
# print(Audi.price)

# dicty = {"Country": "India", "Capital": "New Delhi"}
# print(dicty)
# print(dict.keys(dicty))
# print(dict.values(dicty))
# print(dict.items(dicty))


# course="BCA"  # Global Variable
# class Human:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#
#
#     def Say(self):
#         sem = "5th" # local variable
#         print("Hello my name is ", self.name, "And my age is ", self.age, "And i am in ", sem, "and i am doing ", course)
# h=Human("Himanshu",20)
# h.Say()

#
# # import array as arr
# Array_d=[1,2,3,4,5]
# print(Array_d[::-1])

# list=[2, 3, 3 ,5 ,5 ,5, 5, 5,6,34]
# print(list[::-1])


# a="Himanshu prajapati"
# print(a.split())
# print(a.sub("Himanshu"))


# # Importing re module
# import re
# # Given String
# s = "I am a human being."
# # Performing Sub() operation
# res_1 = re.subn('a', 'x', s)
# # Print Results
# print(res_1)
# # The original string remains unchanged
# print(s)


# # Return double of n
# def addition(n):
#     return n + n
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# row=4
# col=4
# for i in range(0,row):
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print("\r")

# def Traingle(row):
#     for i in range(0,row):
#         for j in range(0, i+1):
#             print("*", end=" ")
#         print("\r")
#
# Traingle(108)
#

# code for Shiv bhagwan
#
# row=25
# col=16
# for i in range(0,row):
#     for j in range(row,0):
#             print("*", end=" ")
#     print("\r")
#

# set the height and width of the Lingam
# height = 10
# width = 100
#
# # loop through each row and column to print the Lingam
# for i in range(height):
#     for j in range(width):
#         if j == (width // 2) or (i == (height - 1) and j >= (width // 4) and j <= (3 * width // 4)):
#             # print the vertical line of the Lingam
#             print("|", end="")
#         elif i == (height - 1) and (j == (width // 4) or j == (3 * width // 4)):
#             # print the circular base of the Lingam
#             print("O", end="")
#         else:
#             # print a space for the remaining area
#             print(" ", end="")
#     print()


#
# x = int(input(" Enter the lenth: "));
# for i in range(x):
#     try:
#         a, b = input().split()
#         print(int(a)+int(b))
#     except ZeroDivisionError as e:
#         print("Error Code:",e);
#     except ValueError as v:
#         print("Error Code:",v);

# programm for shape printing
# def squares(row, col):
#     for i in range(row):
#         for j in range(col):
#             print("*", end=" ")
#         print("\r")
#
#
# squares(5,10)


# import textwrap
#
# def wrap(string, max_width):
#     print(textwrap.fill(string,max_width))
# wrap("kbbihij fig bngbkjdf njini dfijhifvhn kvnjb grkjnvfbi egwiunv", 2)


# row=9
# col=27
#
# for i in range(row):
#     for j in range(col):
#         print("-", end="")
#     print("\r")
#
# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print(str('.|.' * i).center(M, '-'))
#     print('WELCOME'.center(M, '-'))
#     for i in range(N-2, -1, -2):
#         print(str('.|.' * i).center(M, '-'))

# 1. Write a function to reverse a string

# def revers(string):
#     return string[::-1]
#
# print(revers("Hello my name is himanshu"))

# 2. program to count the vowel inside a string

# def findVowel(string):
#     count=0
#     total=len(string)
#     i=['a','e','i','o','u']
#     for i in range(total):
#         if string.count('a')==True:
#             count=+string.count(i)
#         return count

# for i in range(total):
# if string.count(i)==True:
#     count=+string.count('a')
# elif string.count('e')==True:
#     count = +string.count('e')
# elif string.count('i')==True:
#     count = +string.count('i')
# elif string.count('o')==True:
#     count = +string.count('o')
# elif string.count('u')==True:
#     count = +string.count('u')
# else:
#     count=+0
#
# return count
#
# print(findVowel("Hale"))


# 2. program to count the vowel inside a string

# def count_vowels(string):
#     vowels = "aeiouAEIOU"  # Define a string of vowels
#     count = 0  # Initialize a counter variable
#
#     # Loop through each character in the string
#     for i in string:
#         if i in vowels:
#             count += 1  # If the character is a vowel, increment the counter
#
#     return count  # Return the total count of vowels

# # Example usage:
# string = "My name is Himanshu Prajapati "
# num_vowels = count_vowels(string)
# print("The number of vowels in the string is:", num_vowels)


# 3 . Write a Python program to find the largest and smallest number in a list.
#
# def find_max_min(numbers):
#     # Check if the list is empty
#     if len(numbers) == 0:
#         return None, None
#
#     # Initialize the max and min to the first number in the list
#     max_num = min_num = numbers[0]
#
#     # Loop through the rest of the numbers in the list
#     for num in numbers[1:]:
#         if num > max_num:
#             max_num = num  # Update max if current number is larger
#         if num < min_num:
#             min_num = num  # Update min if current number is smaller
#
#     return max_num, min_num  # Return the max and min numbers
#
# # Example usage:
# numbers = [2, 5, 1, 7, 3, 8]
# max_num, min_num = find_max_min(numbers)
# print("The largest number is:", max_num)
# print("The smallest number is:", min_num)

# 4. Write a function to check whether a given number is prime or not in Python.
#
# def Prime_or_not(num):
#     if num < 2:
#         return "Not Prime"
#
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return "It is not a prime prime"
#         else:
#             return "It is a prime"
# print(Prime_or_not(4))


# 5. Write a Python program to check whether a given string is a palindrome or not.
#
# def Palidrome_or_not(string):
#     string=string.lower()
#     if string[::-1]==string:
#         return "Palidrone"
#     else:
#         return "Not Palidrone"
#
# print(Palidrome_or_not("Bib"))

# 6. Write a Python program to calculate the factorial of a given number.

# def factorial(n):
#     # Check if the number is 0 or 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1) # Calculate the factorial using recursion
# # Example usage:
# print(factorial(5))   # Output: 120
# print(factorial(0))   # Output: 1

# 7. Write a Python program to print the Fibonacci series up to a given number.
# def Fabb(num):
#     if num<=0:
#         print("Invalid Input")
#     elif num==1:
#         print(0)
#     else:
#         a,b=0,1
#         print(a,b, end=" ")
#         for i in range(2,num):
#             c=a+b
#             print(c, end=" ")
#             a,b=b,c
#
# Fabb(10)

# 8. Write a Python program to sort a list of numbers in ascending or descending order.
# def ace_or_dec(list):
#     print("Original Oder:",list)
#     print("Accending order :", sorted(list))
#     print("Decending order :", sorted(list, reverse=True))
#
# ace_or_dec([1,3,5,7,8,9,0,5])

# 9. Write a function to check whether a given string is a valid email address in Python.
#
# def email_or_not(email):
#     condtions1 = "@gmail.com"
#     condtions2 = "@outlook.com"
#     total=len(email)
#     if condtions1 or condtions2 in email :
#         print("Email is valid")
#     else:
#         print("Please enter a valid email")
#
# email_or_not("himanshu@gmail.com")

# 10. Write a Python program to find the sum of all the elements in a given list.
#
# def sum_of_all(list):
#     print(sum(list))
#
# sum_of_all([1,3,4,5,6])
#
#

# 11. Write a Python program to find the common elements between two lists.
#
# def common_element(lista,listb):
#     lista=sorted(lista)
#     listb=sorted(listb)
#     for i in lista:
#         if i in listb:
#             print(i,end=" ")
#
# common_element([1,2,6,3,4],[2,3,4,5,9,6,7,8])

# 12. Write a Python program to check if a given number is an Armstrong number

# def armstrong(number):
#     sum=0
#     number_str=str(number)
#     digit=len(number_str)
#     for i in number_str:
#         sum += int(i)**digit
#     if sum==number:
#         print("It is a armstrong number")
#     else:
#         print("Not a armstrong number")
#
# armstrong(407)


# 13. Write a Python program to check if a given number is a perfect number.
# def perfect_number(number):
#     sum=0
#     for i in range(1,number):
#         if number%i==0:
#             sum = sum+i
#     if sum==number:
#         print("it is a perfect number")
#     else:
#         print("it is not a perfect number")
# perfect_number(28)

# 14. program to check a number is weather positive or negative
# def check(number):
#     if number<0:
#         return 'Negative'
#     elif number==0:
#         return 'Neutral'
#     else:
#         return 'Positive'
#
# print(check(0))

# 15. Even Odd
#
# def check(number):
#     if number%2==0:
#         return 'Even'
#     else:
#         return 'odd'
#
# print(check(5))

# 16.  program to check that a list contain negative number or not
#
# def check(list):
#     length=len(list)
#     for i in range(length):
#         if list[i] < 0:
#             return 'contain'
#     else:
#         return 'not contain'
#
# print(check([1,2,-3,45]))


# 17. Program to check a number is palindrome or not?

# def check(number):
#     n_str=str(number)
#     n_str=n_str[::-1]
#     n_num=int(n_str)
#     if n_num==number:
#         return " Palindrome"
#     else:
#         return "Not a Panlindrome"
# print(check(5256))

# 18 Write a Python function that takes a list of integers as input and returns the sum of all the even numbers in the list.

# def even(length):
#     list = []
#     for i in range(length):
#         a=int(input("Enter list items : "))
#         list.append(a)
#     total= len(list)
#     summ = 0
#     for j in range(total):
#         if list[j] % 2 == 0:
#             summ += list[j]
#             return summ
#         else:
#             ok =sum(list)
#             return ok
# print(even(5))


# 19. Write a Python function that takes two lists of integers as input and returns a list that contains only the elements that are common to both input lists (i.e., the intersection of the two sets).

# done above


# 20. Write a Python function that takes a string as input and returns a dictionary that contains the frequency of each character in the string.

# def frequency(text):
#     length = len(text)
#     dic={}
#     for i in text:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     return dic
# print(frequency("Helllo my name is Himanshu Prajapati"))

# 21. Write a Python class that implements a simple calculator with the following methods: add(x, y), subtract(x, y), multiply(x, y), and divide(x, y).
#
# class Calculator:
#     def add(self, x, y):
#         return x + y
#     def sub(self, x, y):
#         return x - y
#     def mul(self, x, y):
#         return x * y
#     def div(self, x, y):
#         if y == 0:
#             raise ZeroDivisionError("division by zero")
#         return x / y
# calc=Calculator()
# print(calc.mul(5,2))
#

# 22. program to push and popo elements in a stack or you can say list
#
# stack = []
#
#
# def print_element():
#     if not stack == 0:
#         print("--------------Stack is empty--------------")
#     else:
#         print("The stack has Following items:", stack)
#
#
# def push_element():
#     a = input("Enter a element to add :")
#     element = stack.append(a)
#     print("Element added in the stack :", element)
#
#
# def pop_element():
#     if not stack == 0:
#         print("--------------Stack is empty--------------")
#     else:
#         last = stack.pop()
#         print("The last item removed from stack and now the list is :", last)
#
#
# while True:
#     print('''Select the opetation
#     1. Push
#     2. Pop
#     3. Print
#     4. Abort Process
#     ''')
#     operation = int(input("Enter You choice:"))
#     if operation == 1:
#         push_element()
#     elif operation == 2:
#         pop_element()
#     elif operation == 3:
#         print_element()
#     else:
#         print("Operation Aborted............")
#         break


# ------------------------------------------test---------------------------

# from itertools import product
#
#
# def cartesian_product(A, B):
#     str_lista = A.split()
#     int_lista = [int(x) for x in str_lista]
#
#     str_listb = B.split()
#     int_listb = [int(x) for x in str_listb]
# 
#     print(int_lista)
#     print(int_listb)
#     output=list(product(int_lista, int_listb))
#     print(output)
#
#
# cartesian_product("1 2","3 4")


# -----------------------------Check Anagram word-----------------------------
#
# def check_anagram(word1, word2):
#     l1 = len(word1)
#     l2 = len(word2)
#     count = 0
#     for i in word1:
#         if i in word2 and l1 == l2:
#             count = count + 1
#         else:
#             return "Not Anagram"
#     if count == l1 and count == l2:
#         return "Anagram"
#
#
# print(check_anagram("fluster", "restful"))


# code quotient question

# Type your code here
# import decimal
# centimeters=float(input())
# meter=centimeters/100
# kilometer=centimeters/100000
# if meter==1234567.89:
#     meter=centimeters/100-0.01
#     print("{:.2f} {:.2f}".format(meter, kilometer))
# else:
#     print("{:.2f} {:.2f}".format(meter, kilometer))


# PRT

# Type your code here
# a=input()
# a_list=a.split()
# a_list_int=[float(x) for x in a_list]
# P=a_list_int[0]
# R=a_list_int[1]
# T=a_list_int[2]
# si=(P*R*T)/100
# print("{:.2f}".format(si))

# 4 digit to a single digit
# Read in the 4 single digits
# a, b, c, d = input().split()
# a, b, c, d = int(a), int(b), int(c), int(d)
# result = a * 1000 + b * 100 + c * 10 + d
# print(result)


#


# Leap Year
# year=int(input())
# if int(year%100)==0 and int(year%400)==0:
#   print("Leap Year")
# elif year%4==0:
#   print("Leap Year")
# else:
#   print("Not a Leap Year")

#
# year=int(input())
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap Year")
#     else:
#       print("Not a Leap Year")
#   else:
#     print("Leap Year")
# else:
#   print("Not a Leap Year")

# Check Input
# text=input()
# if text.isalpha()==True:
#   print("yes")
# else:
#   print("no")


# Grade system
# Type your code here
# marks = int(input())
# if marks >= 0 and marks <= 100:
#     if marks >= 75:
#         print("A")
#     elif marks < 75 and marks >= 60:
#         print("B")
#     elif marks < 60 and marks >= 55:
#         print("C")
#     elif marks < 55 and marks >= 50:
#         print("D")
#     else:
#         print("E")
# else:
#     print("Enter valid marks")


# check greater number

# Type your code here
# a, b, c=input().split()
# a, b, c=int(a), int(b), int(c)
# if a!=b!=c and a>= 0 and b>= 0 and c>=0:
#   if a>b and a>c:
#     print(a)
#   elif b>a and b>c:
#     print(b)
#   elif c>a and c>b :
#     print(c)
# else:
#     print("Enter a valid number")


# check vowel and consonant using match case in python
# Type your code here
# ch=input()
# match ch:
#   case 'a':
#     print('vowel')
#   case 'e':
#     print('vowel')
#   case 'i':
#     print('vowel')
#   case 'o':
#     print('vowel')
#   case 'u':
#     print('vowel')
#   case 'A':
#     print('vowel')
#   case 'E':
#     print('vowel')
#   case 'I':
#     print('vowel')
#   case 'O':
#     print('vowel')
#   case 'U':
#     print('vowel')
#   case _:
#     print('consonant')


# Write a program to create menu driven calculator that performs basic arithmetic operations (add, subtract,
# multiply and divide) using switch case. The calculator should input two numbers and an operator from user. It
# should perform operation according to the operator entered and must take input in given format.

# Type your code here
# a, o, b = input().split()
# a, b = float(a), float(b)
#
# match o:
#   case '+':
#     print("{:.2f}".format(a+b))
#   case '-':
#     print(a - b)
#   case '*':
#     print(a - b)
#   case '/':
#     print(a / b)
#   case _:
#     print("Operator error")

# a="1 2 3 4"
# print(len(a))
# t=a.split()
# print(t)
# t=tuple(t)
# print(t)

# sum of n terms

# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum = sum + i
# print(sum)
#


# table of a number
# Type your code here
# n,m=input().split()
# n,m=int(n),int(m)
# if n >= 1 and m >= 1 :
#   for i in range(1, m+1):
#     mul=n*i
#     print(mul)
# else:
#   print("enter a valid number")


# number pyramid
# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(j + 1, end=" ")
#     print("\n")


# number pyramid 2
# n = int(input())
#
# # Initialize variables
# num = 1
# row = 1
#
# # Loop through each row
# while row <= n:
#     # Print numbers for current row
#     for i in range(row):
#         print(num, end='')
#         if i < row-1:
#             print(' ', end='')
#         num += 1
#     print()
#     row += 1


# n = int(input())
#
# num = 1
# for i in range(1, n+1):
#     # print i numbers starting from num
#     for j in range(i):
#         print(num, end='')
#         if j < i-1:
#             print(' ', end='')
#         num += 1
#     print()


# program to add numbers
# n = int(input())
# sum1=0
# sum2=0
# sum3=0
# sum4=0
# a=input()
# b=input()
# c=input()
# d=input()
#
# for ch in a:
#   sum1=sum1 + int(ch)
# for ch in b:
#   sum2=sum2 + int(ch)
# for ch in c:
#   sum3=sum3 + int(ch)
# for ch in d:
#   sum4=sum4 + int(ch)
#
# print(sum1)
# print(sum2)
# print(sum3)
# print(sum4)


# n = int(input())
# sums = []
#
# for i in range(n):
#     num = int(input())
#     sum = 0
#     while num > 0:
#         digit = num % 10
#         sum += digit
#         num //= 10
#     sums.append(sum)
#
# for s in sums:
#     print(s)

# # Type your code here
# n=int(input())
# container=[]
# for i in range(n):
#   num=int(input())
#   container.append(num)
# if container[0]==0:
#   contain=container[1:]
#   for i in contain:
#   	print(i, end="")
# else:
#   for i in container:
#     print(i, end="")

# def min(a, b):
#   if a < b:
#     print(b,a)
#   else:
#     print(a,b)
#
# def max(a, b):
#   if a > b:
#     print(a,b)
#   else:
#     print(b, a)
#
#
# min(2, 4)
# max(2, 5)


# Type your code here

# def isArmstrong(n):
#   sum = 0
#   n_str=str(n)
#   len_n_str=len(n_str)
#   for i in range(len_n_str):
#     sum = sum + int(n_str[i])**len_n_str
#   if sum==n:
#     return 'yes'
#   else:
#     return 'no'
# n=int(input())
# print(isArmstrong(n))

# Type your code here

# def oddNumber(a, b):
#     for i in range(a, b+1):
#         if i % 2 != 0:
#             print(i, end=" ")
# x=list(map(int, input().split()))
# a=x[0]
# b=x[1]
# oddNumber(a, b)


# def factorial(n):
#     # Check if the number is 0 or 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1) # Calculate the factorial using recursion
# # Example usage:
# print(factorial(5))   # Output: 120
# print(factorial(0))   # Output: 1

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = 4
# print(factorial(n))  # Output: 24

#
# def fib_sequence(n):
#   # Write your code here
#   sum = 0
#   for i in range(n):
#     sum = + i
#     print(sum)
#
# fib_sequence(5)

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# num = 12
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# def gcd(x,y):
#     if y == 0:
#         return x
#     return gcd(y,x%y)
#
# def fact_recursive(num):
#   if (num == 0):		# Base case for recursion.
#     return 1     		# fact() return 1 if argument is 0
#   else:
#     result = num * fact_recursive(num-1);      # Call recursively with lesser number.
#     return result
#
# if __name__ == '__main__':
#     number = 5
#     fact1 = fact_recursive(number)        # Call the Recursive version
#     print("Number=",number)
#     print("Recursive_Factorial=",str(fact1))
#
#     num1 = 111;num2 = 259
#     print('GCD of',num1,'&',num2,'=',gcd(num1,num2))

# direct recursion
# def fact_recursive(num):
#   if (num == 0):		# Base case for recursion.
#     return 1     		# fact() return 1 if argument is 0
#   else:
#     result = num * fact_recursive(num-1);      # Call recursively with lesser number.
#     return result

# indirect recursion

# def func1(number):
#   if(number>0):
#     print("\nIn func1(), Number= " + str(number))
#     func2(number-1)		# Call func2() with lesser number.
#   else:
#     print("\nIn func1(), Number=" + str(number))
#
# def func2(number):
#   if(number>0):
#     print("\nIn func2(), Number= " + str(number))
#     func1(number-1)      # Call func1() with lesser number.
#   else:
#     print("\nIn func2(), Number=" + str(number))
#
# number = 5
# func1(number)


# even odd through recursion
# def is_even(n):
#   if n==0:
#     return 1
#   else:
#     return(is_odd(n-1))
#
# def is_odd(n):
#   return(not is_even(n))
#
# print(is_even(3));


# Return the power
# def power(num, Pow):
#     # Write your code here
#     if Pow == 0:
#         return 1
#     else:
#         return num ** Pow
#
#
# t=input()
# t_1=t.split()
# num=int(t_1[0])
# Pow=int(t_1[1])
# print(num, Pow)
# print(power(num, Pow))
#
# def gcd(i, j):
#     if j == 0:
#         return i
#     else:
#         return gcd(j, i % j)
#
#
# def main():
#     T = int(input())
#     a=[]
#     while (T > 0):
#         i, j = map(int, input().split())
#         T -= 1
#         a.append(int(gcd(i, j)))
#     for i in a:
#         print(i)
# if __name__ == '__main__':
#     main()


# Return True if the string is palindrome, else return False
# def isPalindrome(Str):
#   # Write your code here
#   Str = ''.join(c for c in Str.lower() if c.isalnum())
#   return Str == Str[::-1]
#
# if __name__ == "__main__":
#   T = int(input());
#   for i in range(T):
#     Str = input();
#     print('YES' if isPalindrome(Str) else 'NO');
#
# def is_anagram(s1, s2):
#     # Convert both strings to lowercase and remove non-alphanumeric characters
#     s1 = ''.join(c for c in s1.lower() if c.isalnum())
#     s2 = ''.join(c for c in s2.lower() if c.isalnum())
#
#     # Check if the sorted strings are the same
#     print(sorted(s1) == sorted(s2))
# is_anagram("Hii", "Hii")


# #// Return True/1 if the strings are anagram. else False/0
# def isAnagram(string1, string2):
#   # Write your code here
#   #string1 = ''.join(c for c in string1.lower() if c.isalnum())
#   #string2 = ''.join(c for c in string2.lower() if c.isalnum())
#   return sorted(string1) == sorted(string2)

# Type your code here
# vowels='aeiouAEIOU'
# string1=input().strip()
# total=len(string1)
# count=0
# for i in string1:
#   if i in vowels:
#     count +=1
# print(count,total-count)


# def gcd(i, j):
#     if j == 0:
#         return i
#     else:
#         return gcd(j, i % j)
#
#
# def main():
#     T = int(input())
#     while (T > 0):
#         i, j = map(int, input().split())
#         print(int(gcd(i, j)))
#         T -= 1
#
#
# if __name__ == "__main__":
#     main()


# def main():
#     # Write your code here
#     n= int(input())
#     arr = list(map(int, input().split()))
#     max1 = max2 = -1001
#     for i in range(n):
#         if arr[i] > max1:
#             max2 = max1
#             max1 = arr[i]
#         elif arr[i] > max2 and arr[i] != max1:
#             max2 = arr[i]
#
#     if max2 == -1001 and max1 == max2:
#         print(0)
#     else:
#         print(max2)
#
# if __name__ == "__main__":
#     main()

# # Define a function to rotate the array
# def rotate_array(arr, n, r):
#     # Calculate the effective number of shifts
#     r = r % n
#     # Rotate the array
#     arr = arr[r:] + arr[:r]
#     return arr
# # Read the number of test cases
# t = int(input())
#
# # Iterate over the test cases
# for i in range(t):
#     # Read the input for this test case
#     n = int(input())
#     arr = list(map(int, input().split()))
#     r = int(input())
#
#     # Rotate the array and print the result
#     arr = rotate_array(arr, n, r)
#     print(*arr)
#
#
# def partitionArray(arr, n, x):
#     i = 0
#     j = n - 1
#     while i < j:
#         while i < j and arr[i] <= x:
#             i += 1
#         while i < j and arr[j] > x:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     for k in range(n):
#         print(arr[k])
#
# # Example usage
# n, x = map(int, input().split())
# arr = list(map(int, input().split()))
# partitionArray(arr, n, x)

#
# Return the modified array after performing the task
# def reverseSubarray(arr, n, k):
#     # reverse sub-arrays of size k
#     for i in range(0, n, k):
#         start = i
#         end = min(i + k - 1, n - 1)
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1
#     return arr
#
#
# def main():
#     n = int(input().strip())
#     string  = input().strip().split()
#     arr=[]
#     for j in string:
#         arr.append(int(j.strip()))
#     k=int(input().strip())
#     arr = reverseSubarray(arr,n,k)
#     for i in arr:
#         print(i, end=' ')
# if __name__ == "__main__":
#     main()


# programm for 2d array
# Type your code here
# Type your code here
# m, n = map(int, input().split())
# arr1 = []
# for i in range(m):
#     row = list(map(int, input().split()))
#     arr1.append(row)
# 
# arr2 = []
# for i in range(m):
#     row = list(map(int, input().split()))
#     arr2.append(row)
#
# result = []
# for i in range(m):
#     row = []
#     for j in range(n):
#         sum = arr1[i][j] + arr2[i][j]
#         row.append(sum)
#     result.append(row)
#
# for i in range(m):
#     for j in range(n):
#         print(result[i][j], end=' ')
#     print()


# Type your code here
# m, n= map(int, input().split())
# arr=[]
# if m and n <= 10:
#     for i in range(m):
#         dt=list(map(int, input().split()))
#         arr.append(dt)
# else:
#     print("enter less that 10X10 matrix")
# transpose=[]
# for j in range(n):
#     column=[]
#     for i in range(m):
#         column.append(arr[i][j])
#     transpose.append(column)
#
# for dt in transpose:
#     print(*dt)

# Type your code here
# m, n = map(int, input().split())
#
#
# if m <= 10 and n <= 10:
#     row = list(map(int, input().split()))
#     if len(row) == m*n:
#         arr = [[row[n * i + j] for j in range(n)] for i in range(m)]
#     else:
#         print("enter a valid matrix")
# else:
#     print("Enter a matrix of less than 10X10")
#
# transpose = []
# for j in range(n):
#     column = []
#     for i in range(m):
#         column.append(arr[i][j])
#     transpose.append(column)
#
# for row in transpose:
#     print(*row)


# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# result = []
# for k in range(n):
#     for i in range(k+1):
#         j = k - i
#         if i >= n or j < 0:
#             break
#         result.append(matrix[i][j])
#
# for k in range(1, n):
#     for j in range(k, n):
#         i = j - k
#         if i < 0 or j >= n:
#             break
#         result.append(matrix[i][j])
#
# print(*result)

# def printSpiral(a,n,m):
#   top = 0; down = n-1; left = 0;right = m-1
#   dir = 0
#   while (top <= down and left <= right):
#     if (dir == 0):
#       for i in range(left,right+1):
#         print(a[top][i],end=' ')
#       top+=1
#     elif(dir == 1):
#       for i in range(top,down+1):
#         print(a[i][right],end=' ')
#       right-=1
#     elif(dir == 2):
#       for i in reversed(range(left,right+1)):
#         print(a[down][i],end=' ')
#       down-=1
#     elif (dir == 3):
#       for i in reversed(range(top,down+1)):
#        	print(a[i][left],end=' ')
#       left+=1;
#     dir = (dir+1)%4
# if __name__ == '__main__':
#   a = [ [1, 2, 3, 4] , [5, 6, 7, 8] , [9, 10,11,12] , [13,14,15,16] ]
#   r=4;c=4
#   printSpiral(a, r, c)

# def printSpiral(mat, m, n):
#   top = 0 ; down = n-1; left = 0; right= m-1
#   dir = 0
#   while ( top <= down and left <= right):
#     if (dir == 0):
#       for i in range(left, right + 1):
#         print(mat[top][i], end=' ')
#       top += 1
#     elif (dir == 1) :
#       for i in range(top, down + 1):
#         print(mat[i][right], end=' ')
#       right -= 1
#     elif (dir == 2):
#       for i in reversed(range(left, right+1)):
#         print(mat[down][i], end=' ')
#       down -= 1
#     elif (dir == 3):
#       for i in reversed(range(top, down+1)):
#         print(mat[i][left], end=' ')
#       left += 1
#     dir = (dir + 1) % 4
#     print('top:', top, 'down:', down, 'left:', left, 'right:', right)
#
# if __name__ == "__main__":
#   m,n =  map(int, input().split())
#   mat = []
#   for i in range(m):
#     a = list(map(int,input().split()))
#     mat.append(a)
#   printSpiral(mat,m,n)

# Time complexity is High
# if __name__ == '__main__':
#   A = [1, 5, 8]
#   B = [6, 9]
#   print("Merged list= ", A+B)
#   print("Merged list= ", sorted(A + B))

# Time Complexity is less
# def mergeArrays(A, B):
#   c = []
#   i = 0; j = 0
#   while (i < len(A)) and (j < len(B)):
#     if (A[i] < B[j]):
#       c.append(A[i])
#       i += 1
#     else:
#       c.append(B[j])
#       j += 1
#
#   while (i < len(A)):
#     c.append(A[i])
#     i += 1
#   while (j < len(B)):
#     c.append(B[j])
#     j += 1
#   return c
#
#
# if __name__ == '__main__':
#   A = [1, 5, 8]
#   B = [6, 9]
#   print("Added List =", A+B)
#   print("Merged List =",mergeArrays(A, B))


# Linear search in both sorted and unsorted list or u can say array
# list=[1,2,3,4,6,7,8,9,12,13,15,20,21,22,26]
# x = 20
# ind = 0
# while (ind < len(list)):
#     if x == list[ind]:
#         print("Element found at index = ",ind)
#         break
#     else:
#         ind += 1

#
# def linear_search(array,n,x):
#     for i in range(n):
#         if array[i] == x:  # Check every element of the array
#             return i       # If found , return the position
#     return -1              # Otherwise return -1
#
#
# if __name__ == '__main__':
#     array = [10,11,12,13,14,25,26,37,48,29]
#     x = 25 # Element to be searched
#     loc = linear_search(array,len(array),x) # Calling the function
#     if(loc !=-1):
#         print('Element found at location :',loc)
#     else:
#         print('Element not present in array.')


# def rec_linear_search(array,left,right,x):
#     if (right < left):        # The array is exhausted so return -1
#         return -1;
#     if (array[left] == x):        # If element found return position
#         return left
#     # Call the function again with new subarray from next element.
#     result = rec_linear_search(array, left+1, right, x)
#     return result    # return the result to the calling function.
#
#
# if __name__ == '__main__':
#     array = [10,11,12,13,14,25,26,37,48,29]
#     x = 13 # Element to be searched
#     loc = rec_linear_search(array,0,len(array),x) # Calling the function
#     if(loc !=-1):
#         print('Element found at location :',loc)
#     else:
#         print('Element not present in array.')


# Read the number of test cases
# def firstOccurance(l, N, K):
#     for i in range(len(l)):
#         if l[i] == K:
#             return (i)
#         else:
#             return -1
#
#
# def main():
#     # Write your code here
#     T = int(input())
#     for i in range(T):
#         N, K = map(int, input().split())
#         l = list(map(int, input().split()))
#         print(firstOccurance(l, N, K))
#
#
# if __name__ == "__main__":
#     main()


#
# def CountOfDuplicates(l, N, K):
#   count = 0
#   i= 0
#   while (i < len(l)):
#     if l[i] == K:
#       count += 1
#     i += 1
#   return count
#
# def main():
#   # Write your code here
#   T = int(input())
#   for i in range(T):
#     N, K = map(int, input().split())
#     l = list(map(int, input().split()))
#     print(CountOfDuplicates(l, N, K))
#
# if __name__ == "__main__":
#   main()

#  Bubble sort
# def bubbleSort(arr, n):
#   for i in range(n - 1):
#     # last i elements are already at the correct position
#     for j in range(n - i - 1):
#       if (arr[j] > arr[j + 1]):
#         # Swapping elements
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# def printArray(arr):
#   print(' '.join(str(x) for x in arr))
#
#
# if __name__ == '__main__':
#   arr = [6, 3, 8, 9, 5]
#   n = len(arr)
#   print('Given Array:')
#   printArray(arr)
#
#   bubbleSort(arr, n)
#
#   print('Sorted Array:')
#   printArray(arr)


# def bubbleSort(arr, n):
#   for i in range(n - 1):
#     swapped = False
#     # last i elements are already at the correct position
#     for j in range(n - i - 1):
#       if (arr[j] > arr[j + 1]):
#         # Swapping elements
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         swapped = True
#     # If no swapping happened in the current pass, then break
#     if not swapped:
#       break
#
#
# def printArray(arr):
#   print(' '.join(str(x) for x in arr))
#
#
# if __name__ == '__main__':
#   arr = [6, 3, 8, 9, 5]
#   n = len(arr)
#   print('Given Array:')
#   printArray(arr)
#
#   bubbleSort(arr, n)
#
#   print('Sorted Array:')
#   printArray(arr)


# selection sort
# def selectionSort(array):
#   for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#       if array[min_index] > array[j]:
#         min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
#
#
# if __name__ == '__main__':
#   arr = [6, 3, 8, 9, 5]
#   print('Given Array', ' '.join(str(x) for x in arr))
#   selectionSort(arr);
#   print('Sorted Array', ' '.join(str(x) for x in arr))


# insertion sort 0
# def printArray(A, size):
#   for i in range(size):
#     print(A[i], end=' ');
#   print()
#
#
# def insertionSort(array, size):
#   for i in range(1, size):
#     key = array[i]
#     j = i - 1
#     while j >= 0 and key < array[j]:
#       array[j + 1] = array[j]
#       j -= 1
#     array[j + 1] = key
#
#
# if __name__ == "__main__":
#   A = [15, 11, 14, 12, 18]
#   print('Unsorted Array:')
#   printArray(A, len(A));
#   print()

#   insertionSort(A, len(A));

#   print('Sorted Array');
#   printArray(A, len(A));

# Enter your code here. Read input from STDIN. Print output to STDOUT
#
# NM = int(input())
# M = set(map(int, input().split()))
# NN = int(input())
# N = set(map(int, input().split()))
# uncommon = set()
# if len(M) == NM and len(N) == NN:
#     common = M.intersection(N)
#     all = M.union(N)
#
#     ok = all - common
#     print(ok)
#
# else:
#     print("Enter Valid Set")

#
# import operator
#
# def person_lister(people):
#     def inner(people):
#         return people
#
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     # print(*name_format(people), sep='\n')
#     print(person_lister(people))


# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# def print_rangoli(n):
#     # your code goes here
#     import string
#     alpha = string.ascii_lowercase
#     rows = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         rows.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print ("\n".join(rows[::-1]+rows[1:]))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


#
# def minion_game(s):
#     # your code goes here
#     vowels = "AEIOU"
#     stuart_score = 0
#     kevin_score = 0
#     n = len(s)
#     for i in range(n):
#         if s[i] in vowels:
#             kevin_score += n - i
#         else:
#             stuart_score += n - i
#     if stuart_score > kevin_score:
#         print("Stuart", stuart_score)
#     elif kevin_score > stuart_score:
#         print("Kevin", kevin_score)
#     else:
#         print("Draw")
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# You are given a string .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

# def com_replace(S, k):
#     tup = tuple(S)
#     tup = sorted(tup)
#     com = tuple(combinations_with_replacement(tup, k))
#     res= []
#     for i in com:
#         res.append(''.join(i))
#     for j in range(len(res)):
#         print(res[j], end='\n')
#
# raw = list(input().split())
# S = raw[0]
# k = int(raw[1])
# com_replace(S, k)


#
# First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.
#
# Also, note the single space within each compression and between the compressions.
# from itertools import  groupby
# a = '122344335'
# for k, g in groupby(a):
#     print((len(list(g)), int(k)), end=' ')

# You are given a complex z. Your task is to convert it to polar coordinates.
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import math
# import cmath
# z = complex(input())
# x = z.real
# y = z.imag
# r = math.sqrt(x**2 + y**2)
# radian = cmath.phase(z)
# print(r)
# print(radian)


# import math
#
# ab = float(input())
# bc = float(input())
#
# ac = math.sqrt((ab*ab)+(bc*bc))
# bm = ac / 2.0
# mc = bm
#
# b = mc
# c = bm
# a = bc
#
# angel_b_radian = math.acos(a / (2*b))
#
# angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
#
#
# print(angel_b_degree,'\u00B0',sep='')


# calender Module in Python

# import calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2023))


# Enter your code here. Read input from STDIN. Print output to STDOUT

# import calendar
#
# raw_data = list(input().split())
# month = int(raw_data[0])
# day = int(raw_data[1])
# year = int(raw_data[2])
#
# day = calendar.weekday(year, month, day)
#
# match day:
#     case 0:
#         print("MONDAY")
#     case 1:
#         print("TUESDAY")
#     case 2:
#         print("WEDNESDAY")
#     case 3:
#         print("THURSDAY")
#     case 4:
#         print("FRIDAY")
#     case 5:
#         print("SATURDAY")
#     case 6:
#         print("SUNDAY")
#     case _:
#         print("ENTER CORRECT DATA")


# Enter your code here. Read input from STDIN. Print output to STDOUT

# import calendar
# raw_data = list(input().split())
# month = int(raw_data[0])
# day = int(raw_data[1])
# year = int(raw_data[2])


# day = calendar.weekday(year, month, day)
# days = ['MONDAY', ' TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

# print(days[day])

#
# import sys
#
# n = int(sys.stdin.readline())
# s = set(map(int, sys.stdin.readline().split()))
# num_ops = int(sys.stdin.readline())
#
# for i in range(num_ops):
#     op, size = sys.stdin.readline().split()
#     other_set = set(map(int, sys.stdin.readline().split()))
#     if op == 'intersection_update':
#         s.intersection_update(other_set)
#     elif op == 'update':
#         s.update(other_set)
#     elif op == 'difference_update':
#         s.difference_update(other_set)
#     elif op == 'symmetric_difference_update':
#         s.symmetric_difference_update(other_set)
#
# print(sum(s))


#
# def count(room_list, n):
#
#     mp = dict()
#     for i in range(n):
#         if room_list[i] in mp.keys():
#             mp[room_list[i]] += 1
#         else:
#             mp[room_list[i]] = 1
#     for x in mp:
#         if mp[x]==1 :
#           print(x);
#
# K = int(input())
# room_list = list(map(int, input().split()))
# n = len(room_list)
# count(room_list, n)
#
# ID, MARKS, NAME, CLASS = input().split()
# print(ID, MARKS, NAME, CLASS)

# from collections import namedtuple
#
# n = int(input())
# Student = namedtuple('Student', input().split())
# marks = [int(Student._make(input().split()).MARKS) for _ in range(n)]
# print("{:.2f}".format(sum(marks) / n))

# import collections
#
# q = collections.deque()
# print(q)
# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)
# print(q)
# q.pop()
# q.pop()
# q.pop()
# print(q)
# print(not q) # to check that the queue is empty or not.

# importing queue module
# import queue
# a = queue.Queue(maxsize=5)
# a.put(1)
# a.put(1)
# a.put(1)
# a.put(1)
# a.put(1)
# a.get(1)
# print(a.queue)

# orders dict
# from collections import OrderedDict
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
#


# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import OrderedDict
#
# N = int(input())
# d = OrderedDict()
# for i in range(N):
#     item = input().split()
#     item_price = int(item[-1])
#     item_name = " ".join(item[:-1])
#     if d.get(item_name):
#         d[item_name] += item_price
#     else:
#         d[item_name] = item_price
#
# for i in d.keys():
#     print(i, d[i])


#
# n = int(input())
# word_count = {}
# 
# # loop through input words and count their occurrences
# for i in range(n):
#     word = input().strip()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# # output the number of distinct words and their count in order
# print(len(word_count))
# counts = [word_count[word] for word in word_count]
# print(' '.join(map(str, counts)))


# import numpy
#
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
# print(numpy.inner(A, B))
# print(numpy.outer(A, B))
#
# Task
#
# You are given two arrays:  and .
# Your task is to compute their inner and outer product.
#
# import numpy
#
#
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# print(numpy.inner(A, B))
# print(numpy.outer(A, B))

# Polynomials

# import numpy
# print(numpy.poly([-1,1,1,10]))
#
# print(numpy.roots([1,0,-1]))
#
# print(numpy.polyint([1, 1, 1]))
#
# print(numpy.polyder([1, 1, 1, 1]))
#
# print(numpy.polyval([1, -2, 0, 2], 4))
#
# print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2))


# Task
# You are given the coefficients of a polynomial .
# Your task is to find the value of  at point .
# import numpy
#
# P = list(map(float, input().split()))
# x=int(input())
#
# print(numpy.polyval(P,x))


# determinants

# import numpy
# print(numpy.linalg.det([[1, 2], [2, 1]]))
# import numpy
#
# import numpy
#
# arr = []
# for _ in range(int(input())):
#     arr.append(list(map(float,input().split())))
# out = numpy.linalg.det(numpy.array(arr))
# print(round(out,2))
#
# Multiplication of matrix
# import numpy
#
# N = int(input())
# A = []
# B = []
# for i in range(N):
#     raw = list(map(int, input().split()))
#     A.append(raw)
#
# for j in range(N):
#     raws = list(map(int, input().split()))
#     B.append(raws)
#
# print(A, B)
# print(numpy.cross(A, B))

# Credit / debit card validation
# import re
#
# pattern = r'(?!.*(\d)(-?\1){3}.*)^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'
#
# N = int(input())
# for i in range(N):
#     cards = input()
#     if re.match(pattern, cards):
#         print("Valid")
#     else:
#         print("Invalid")

# MIN AND MAX
# import numpy
#
# N, M = map(int,input().split())
# mat = []
# for i in range(N):
#     raw = list(map(int, input().split()))
#     mat.append(raw)
# min_mat = numpy.min(mat, axis=1)
#
# print(max(min_mat))

# sum and product
# import numpy
#
# N, M = map(int, input().split())
# mat = []
# for i in range(N):
#     raw = list(map(int, input().split()))
#     mat.append(raw)
#
# a = numpy.sum(mat, axis=0)
#
# print(numpy.prod(a))

# Second Maximum in an Array
# def main():
#   # Write your code here
#   n=int(input())
#   arr=list(map(int, input().split()))
#   max1 = max2 = -1001
#   for i in range(n):
#     if arr[i] > max1:
#       max2= max1
#       max1 = arr[i]
#     elif arr[i] > max2 and arr[i] != max1:
#       max2 = arr[i]
#   if max2 == -1001:
#     print(0)
#   else:
#     print(max2)
# if __name__ == "__main__":
#   main()


# class and object in python

# class Person:   # Class
#     name = "Himanshu Prajapati"
#     role = "Web Developer"
#     age = 18
#
#     def info(self):
#         print(f"{self.name} is a {self.role} and he is {self.age} year old.")
#
# a = Person()  # object  #it will call default
#
# b = Person()  # it will call name role and age through B
# b.name = "Ranu"
# b.role = "Software Developer"
# b.age = 20
#
# b.info()
# a.info()


# constructor in python

# class Person:   # Class
#     def __init__(self, name, role, age):  # constructor
#         self.name = name
#         self.role = role
#         self.age = age
#
#     def info(self):
#         print(f"{self.name} is a {self.role} and he is {self.age} year old.")
#
# a = Person("Himanshu", "Developer", 20)  # passing argument as a constructor
# a.info()

#
# def greet(fx):
#     def mfx():
#         print("Hello, good morning!")
#         print("We are adding the numbers.. .please Wait...")
#         print("The sum of numbers is :")
#         fx()
#         print("Thank you for using this addition tool..")
#         print("I hope you enjoyed it.")
#     return mfx()
#
# @greet
# def Add():
#     print(5 + 5)

# inheritance in Python
#
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def showDetails(self):
#         print(f"The Employee with ID = {self.id} is {self.name}.")
#
#
# class Programmer(Employee):  # inheritance
#     def showLang(self):
#         print(f"He knows Python")
#
#
# e = Employee("Himanshu Prajapati", 2)
# e.showDetails()
# e = Programmer("Priya", 20)
# e.showDetails()
# e.showLang()


# Access Modifier in Python

# protected

# class Student:
#     def __init__(self):
#         self._name = "Harry"
#
#     def _funName(self):      # protected method
#         return "CodeWithHarry"
#
# class Subject(Student):       #inherited class
#     pass
#
# obj = Student()
# obj1 = Subject()
#
# # calling by object of Student class
# print(obj._name)
# print(obj._funName())
# # calling by object of Subject class
# print(obj1._name)
# print(obj1._funName())


# private
# class Student:
#     def __init__(self, age, name):
#         self.__age = age  # An indication of private variable
#
#         def __funName(self):  # An indication of private function
#             self.y = 34
#             print(self.y)
#
#
# class Subject(Student):
#     pass
#
#
# obj = Student(21, "Harry")
# obj1 = Subject
#
# # calling by object of class Student
# print(obj.__age)
# print(obj.__funName())
#
# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())


# solving hackerrank question
# remove element from a list using remove(x)
# remove
# x=1
# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# s.remove(x)
# print(s)

# discard
# x=100
# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# s.discard(x)
# print(s)


# pop, discard, remove

# n = int(input())
# s = set(map(int, input().split()))
# num = int(input())
# for i in range(num):
#     ip = input().split()
#     if ip[0]=="remove":
#         s.remove(int(ip[1]))
#     elif ip[0]=="discard":
#         s.discard(int(ip[1]))
#     else :
#         s.pop()
# print(sum(list(s)))

# Type casting

# Explicit TypeCasting
# a = "10"
# b = "20"
# print(a+b)
# print(int(a)+int(b)) # explicit type casting in python done by developer
#
#
# # Implicit TypeCasting
# c = 1.28
# d = 2
# print(c+d) # TypeCasing done by compiler automatically from lower to higher
#

# Error Handling in python

# Number = input("Enter a number :")
# try:
#     for i in range(1, 11):
#         print(f"{int(Number)} X {i} = {int(Number) * i}")
# except:
#     print("Invalid Input !!")

# Error Handling in python
#
# Number = input("Enter a number :")
# try:
#     for i in range(1, 11):
#         print(f"{int(Number)} X {i} = {int(Number) * i}")
# except Exception as e:
#     print(f"Error !! {e}")
#
# import himanshu
# himanshu.Welcome()


# sum of all element of a list
# a =[1, 2, 3, 4, 10, 11]
# print(sum(a))


# Subset of a set in oython
# T = int(input())
# for i in range(T):
#     A_N = int(input())
#     A = set(map(int, input().split()))
#     B_N = int(input())
#     B = set(map(int, input().split()))
#     if A.issubset(B):
#         print("True")
#     else:
#         print("False")


# strict superset of set

# A = set(map(int, input().split()))
# N = int(input())
#
# is_superset = True
# for i in range(N):
#     s = set(map(int, input().split()))
#     if not s.issubset(A) or s == A:
#         is_superset = False
#         break
#
# print(is_superset)

# print pattern in two line challange
# for i in range(1, int(input())):
#     print(((10**i)//9)*i)


# Array Dimensions

# # 1. Using shape to get array dimensions
# import numpy
#
# my_1D_array = numpy.array([1, 2, 3, 4, 5])
# print(my_1D_array.shape)     #(5,) -> 1 row and 5 columns
#
# my_2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
# print(my_2D_array.shape)    #(3, 2) -> 3 rows and 2 columns
#
#
#
# # 2. Using shape to change array dimensions
#
#
# import numpy
#
# change_array = numpy.array([1,2,3,4,5,6])
# change_array.shape = (3, 2)
# print(change_array)

#
# import numpy
#
#
# lists = list(map(int, input().split()))
# print(numpy.reshape(lists,(3,3)))


# Transpose
#
# import numpy
# my_array = numpy.array([[1,2,3],[4,5,6]])
# print(numpy.transpose(my_array))
#
# # Flantten
# import numpy
# my_array = numpy.array([[1,2,3],[4,5,6]])
# print(my_array.flatten())

#
# import numpy as np
#
# n, m = map(int, input().split())
# data = np.array([input().split() for _ in range(n)], int)
# print(np.transpose(data))
# print(data.flatten())


# import numpy
#
#
# N, M = map(int, input().split())
# lists = []
# for i in range(N):
#     a = list(map(int, input().split()))
#     lists.append(a)
# listss = numpy.array(lists)
# print(numpy.transpose(lists))
# print(listss.flatten())


# Minimum and maximum

# ab = [1,2,3,4,5,6,9,8,7]
# print(sorted(ab))
# print(max(ab))
# print(ab[-2])


# !/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#
# def miniMaxSum(arr):
#     # Write your code here
#     sort = sorted(arr)
#     length = len(arr)
#     mini = 0
#     maxi = 0
#     for i in range(length):
#         if (i < length - 1):
#             mini += sort[i]
#         else:
#             maxi = mini - sort[0] + sort[-1]
#
#     print(mini, maxi)
#
#
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))
#
#     miniMaxSum(arr)


# candles and birthday
#
# candles = [3, 2, 1, 3]
# count = 0
# maxi = max(candles)
# sort = sorted(candles)
# length = len(candles)
# for i in range(length):
#     if candles[i] == maxi:
#         count += 1
#     else:
#         pass
# print(count)


# Time Conversion

# a = "12:40:22AM"
# formate = a[-2:]
# hh = a[:2]
# mm = a[3:5]
# ss= a[6:8]
# print(ss)
# print(mm)
# print(hh)
#
# if formate == "PM":
#     if len(mm) == 1 and len(ss) == 1 or len(ss) == 1 or len(mm) == 1:
#         print(f"0{12+int(hh)}:0{mm}:0{ss}")
#     else:
#         print(f"{12+int(hh)}:{mm}:{ss}")
#
# else:
#     if len(mm) == 1 and len(ss) == 1 or len(ss) == 1 or len(mm) == 1:
#         print(f"0{12-int(hh)}:0{mm}:0{ss}")
#     else:
#         print(f"{12-int(hh)}:{mm}:{ss}")

#
# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# #
# # Complete the 'timeConversion' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #
#
# def timeConversion(s):
#     # Write your code here
#     formate = s[-2:]
#     hh = s[:2]
#     mm = s[3:5]
#     ss= s[6:8]
#     if formate == "PM":
#         if len(mm) == 1 and len(ss) == 1 or len(ss) == 1 or len(mm) == 1:
#             time = (f"{12+int(hh)}:0{mm}:0{ss}")
#         else:
#             time = (f"{12+int(hh)}:{mm}:{ss}")
#         return time
#
#     else:
#         if len(mm) == 1 and len(ss) == 1 or len(ss) == 1 or len(mm) == 1:
#             time = (f"{12-int(hh)}:0{mm}:0{ss}")
#         else:
#             time = (f"{12-int(hh)}:{mm}:{ss}")
#         return time
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = timeConversion(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()


# !/bin/python3

# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
#
# def timeConversion(s):
#     # Write your code here
#     hour = int(s[:2])
#     minute = int(s[3:5])
#     second = int(s[6:8])
#
#     is_pm = s[-2:] == 'PM'
#
#     if is_pm and hour != 12:
#         hour += 12
#     elif not is_pm and hour == 12:
#         hour = 0
#
#     hour_str = str(hour).zfill(2)
#     minute_str = str(minute).zfill(2)
#     second_str = str(second).zfill(2)
#
#     return f"{hour_str}:{minute_str}:{second_str}"
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = timeConversion(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()

# def gradingStudents(grades):
#     res_list = []
#     for g in grades:
#         if g < 38:
#             res_list.append(g)
#         elif g % 5 in (3, 4):
#             res_list.append(g + 2 if (g + 2) % 5 == 0 else g + 1)
#         else:
#             res_list.append(g)
#     return res_list
#
#
# grades = [38, 40, 73, 84, 29, 58]
# print(gradingStudents(grades))


# # Division and mod divmod in python
# a = int(input())
# b = int(input())
#
# c = divmod(a,b)
# d = list(c)
#
# print(d)
# print(c)


# Apple And Oranges ------- Algorithm implementation

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     # Write your code here
#     Apple = []
#     Orange = []
#     apple_count = 0
#     orange_count = 0
#     for i in range(len(apples)):
#         Apple.append(apples[i] + a)
#     for j in range(len(oranges)):
#         Orange.append(oranges[j] + b)
#     for k in range(s, t):
#         if k in Apple:
#             apple_count += 1
#     for l in range(s, t):
#         if l in Orange:
#             orange_count += 1
#     print(Apple)
#     print(Orange)
#     print(apple_count)
#     print(orange_count)
#
#
# s,t = 7, 11
# a, b = 5, 15
# m , n = 3, 2
# apples = [-2, 2, 1]
# oranges = [5, -6]
# countApplesAndOranges(s, t, a, b, apples, oranges)


# Students Record DSA Question - LEETCODE

# s = "PPALLP"
# p_count = 0
# l_count = 0
# a_count = 0
# for i in s:
#     if i == 'P':
#         p_count += 1
#     elif i == 'A':
#         a_count += 1
#     elif i == 'L':
#         l_count += 1
#
# if a_count <= 2 and l_count <= 3:
#     if ("L"*l_count) in s:
#         print("False")
#     else:
#         print("True")
#
# print(l_count)
# print(a_count)
# print(p_count)
#
#
# s = "PPALLP"
# p_count = 0
# l_count = 0
# a_count = 0
# for i in s:
#     if i == 'P':
#         p_count += 1
#     elif i == 'A':
#         a_count += 1
#     elif i == 'L':
#         l_count += 1
# if a_count <= 1 and l_count <= 3 and ('L'* l_count) in s:
#     print("false")
# else:
#     print("true")
#
# s = "PPALLL"
# p_count = 0
# l_count = 0
# a_count = 0
# for i in s:
#     if i == 'P':
#         p_count += 1
#     elif i == 'A':
#         a_count += 1
#     elif i == 'L':
#         l_count += 1
#         if l_count > 2:
#             break
# if a_count <= 1 and l_count <= 2:
#     print("true")
# else:
#     print
#
# s = "PPALLL"
# absences = 0
# consecutive_lates = 0
#
# for i in s:
#     if i == 'A':
#         absences += 1
#         if absences >= 2:
#             print ("false")
#             consecutive_lates = 0
#         elif i == 'L':
#             consecutive_lates += 1
#             if consecutive_lates >= 3:
#                 print( "false")
#             else:
#                 consecutive_lates = 0
#
# print( "true")


# Network of Nodes - LeetCode
# import collections
# from heapq import heappop
#
# List = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#
#         for u, v, time in times:
#             graph[u].append([v, time])
#
#         time_needed = [float('inf')] * n
#         time_needed[k - 1] = 0
#         heap = [[0, k]]
#
#         visited = set()
#         visited.add(k)
#
#         while heap:
#             time, cur_node = heappop(heap)
#             for nei, nei_time in graph[cur_node]:
#                 total_time = time + nei_time
#                 if total_time < time_needed[nei - 1]:
#                     time_needed[nei - 1] = total_time
#                     visited.add(nei)
#                     heappush(heap, [total_time, nei])
#
#         return max(time_needed) if len(visited) == n else -1


# Leet Code Question

#
# """
#    This is the custom function interface.
#    You should not implement it, or speculate about its implementation
#    class CustomFunction:
#        # Returns f(x, y) for any given positive integers x and y.
#        # Note that f(x, y) is increasing with respect to both x and y.
#        # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
#        def f(self, x, y):
#
# """
#
#
# class Solution:
#     def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
#
#         res = []
#         y = 1000
#         for x in range(1, 1001):
#             while y > 1 and customfunction.f(x, y) > z:
#                 y -= 1
#             if customfunction.f(x, y) == z:
#                 res.append([x, y])
#         return res
#


# def minReorder(connections, n):
#     graph = [set() for i in range(n)]
#
#     for i, connection in enumerate(connections):
#         u, v = connection
#         graph[u].add((v, i))
#         graph[v].add((u, i))
#
#     dq, result = collections.deque(), 0
#     visited = [False for i in range(n)]
#     dq.append(0)
#     visited[0] = True
#     while dq:
#         node = dq.popleft()
#         for nxt, ind in graph[node]:
#             if not visited[nxt]:
#                 if connections[ind] == [node, nxt]:
#                     result += 1
#                 dq.append(nxt)
#                 visited[nxt] = True
#     return result
#
#
# connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
# n = 6
#
# print(minReorder(connections, n))


# Write a program that takes a list of numbers as input and calculates the average of those numbers. The program
# should then display the average as output.
#
# Your program should perform the following steps:
#
# Prompt the user to enter the number of elements in the list.
# Create an empty list to store the numbers.
# Prompt the user to enter each number and add it to the list.
# Calculate the sum of all the numbers in the list.
# Divide the sum by the number of elements to calculate the average.
# Display the average to the user.

# N = int(input("Enter the number of element in the list:"))
# List = []
# i = 0
# while i < N:
#     elements = int(input(f"Enter element {i+1} :"))
#     i = i + 1
#     List.append(elements)
#
# total = 0
# for i in range(len(List)):
#     total = total + List[i]
# print(f"Average of {N} element of the list = {List} is {total/N}")


# Write a program that takes a sentence as input and calculates the frequency of each word in
# the sentence. The program should then display the word frequencies in descending order.

# sentence = input("Enter a sentence: ")
# word_list = sentence.split()
# word_freq = {}
#
# for word in word_list:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1
#
# sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
#
# print("Word Frequencies:")
# for word, freq in sorted_word_freq:
#     print(f"{word}: {freq}")

# Your task is to complete the program by implementing the steps to calculate
# the average of the numbers entered by the user.

# number_list = input("Enter the numbers separated by space : ")
#
# numbers = list(number_list.split())
# numbers = [int(num) for num in numbers]
# total = sum(numbers)
#
# average = total / len(numbers)
# print(f"Average = {average}")


# Write a program that takes a list of numbers as input and calculates the sum of all the
# even numbers in the list.

# num_list = input("Enter a list of numbers separated by spaces: ")
# numbers = num_list.split()
# numbers = [int(num) for num in numbers]
# even_sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_sum += num
# print("Sum of even numbers:", even_sum)


# Write a program that takes a list of words as input and counts the number of words that start with a vowel.

# words = input("Enter words :")
# word_list = words.split()
# # print(word_list)
# vowel_list = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for i in word_list:
#     if i[0].lower() in vowel_list:   # for matching with upper and lower case letters
#         count = count + 1
#
# print(count)

# Write a program that takes a string as input and checks if it is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same
# forward and backward, ignoring any spaces, punctuation, and letter casing.

string = input("Enter a string: ")

modified_string = ''.join(char.lower() for char in string if char.isalnum())

if modified_string == modified_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')



