#Write a program for assignment operators and explain each
a=22
b=33
c=a+b
print(c)

a+=b #Add right side operand with left side operand and then assign the result to left operand
print(a)

a-=b #Subtract right side operand from left side operand and then assign the result to left operand
print(a)

a*=b #Multiply right operand with left operand and then assign the result to the left operand
print(a)

a/=b #Divide left operand with right operand and then assign the result to the left operand
print(a)

a%=b #Divides the left operand with the right operand and then assign the remainder to the left operand
print(a)

a//=b #Divide left operand with right operand and then assign the value(floor) to left operand
print(a)

a**=b #Calculate exponent(raise power) value using operands and then assign the result to left operand
print(a)

#Write a program for arithmatic , logical , membership operators and explain use of each
#Arithmetic Operators
a=23
b=44
c=a+b #adds two operands
print(c)

x=11
y=55
z=x-y #subtracts two operands
print(z)

z=x*y # multiplies two operands
print(z)

z=x%y
#returns the remainder when the first operand is divided by the second
print(z)

z=x/y
#divides the first operand by the second
print(z)

z=x//y #
#divides the first operand by the second
print(z)

z=x**y
print(z)#Returns first raised to power second

#Comparison
print(x>y)#True if the left operand is greater than the right

print(x<y) #True if the left operand is less than the right

print(x==y) #True if both operands are equal

print(x!=y) #Not equal to – True if operands are not equal

print(x>=y) #Greater than or equal to True if the left operand is greater than or equal to the right

print(x<=y) #Less than or equal to True if the left operand is less than or equal to the right

#Logical Operators
print(a and b) #Logical AND: True if both the operands are true

print(a or b) #Logical OR: True if either of the operands is true

print(not a) #Logical NOT: True if the operand is false

#Membership Operators
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
  print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


#Calculate the area of a circle.

import math

def area_of_circle(radius):
    return math.pi * radius ** 2
radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area_of_circle(radius))

#Calculate the area of a triangle.
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#Calculate the area of a rectangle.
width=5  
height=10  
area=width*height  
print("Area of rectangle="+str(area))

# Calculate the area of a square.
s=13  
area_square=s*s  
print("Area of the square="+str(area_square))  
