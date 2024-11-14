#Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
x=int(input("enter the number:"))
if(x%2)==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")


#Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
age = int(input("Enter age : "))

if age >= 18:
    print("Eligible for Voting!")
else:
    print("Not Eligible for Voting!")

#Write a Python program that determines if a given year is a leap year or not.
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")


#Create a Python program that checks if a user-given number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


#Write a Python program that determines the largest of three numbers entered by the user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
