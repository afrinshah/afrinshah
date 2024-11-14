Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#print helloworld
print("hello world")
hello world

#Declare text data type variable and show the maximum size of text type in python
import sys
>>> txt_variable="how declare text data type variable"
>>> max_size=sys.maxsize
>>> print(f"maximum size of text type:{max_size}")
maximum size of text type:9223372036854775807
>>> 
>>> # Write a code that show types and size of numeric data type (i.e int, float,complex)
>>> int_var=23456
>>> float_var=3534.23
>>> complex_var=2455 +6578j
>>> print(f"type of int_var:{type(int_var)},Size:{sys.getsizeof(int_var)} bytes")
type of int_var:<class 'int'>,Size:28 bytes
>>> 
>>> print(f"type of float_var:{type(float_var)},Size:{sys.getsizeof(float_var)} bytes")
type of float_var:<class 'float'>,Size:24 bytes
>>> print(f"type of complex_var:{type(complex_var)},Size:{sys.getsizeof(complex_var)} bytes")
type of complex_var:<class 'complex'>,Size:32 bytes
>>> 
>>> #Write a code for boolean type and the max size it holds
>>> bool_var_true=True
>>> bool_var_false=False
>>> print(f"type of bool_var_true:{type(bool_var_true)},Size:{sys.getsizeof(bool_var_true)} bytes")
type of bool_var_true:<class 'bool'>,Size:28 bytes
>>> print(f"type of bool_var_false:{type(bool_var_false)},Size:{sys.getsizeof(bool_var_false)} bytes")
type of bool_var_false:<class 'bool'>,Size:28 bytes
>>> 
>>> #Write a program to declare various ways to declare a complex number and check which s real and which is imaginary
>>> import cmath
>>> complex_num1=33
>>> complex_num2=5j
>>> complex_num3=complex(complex_num1,complex_num2)
>>> print("The real part of complex number is:", complex_num3.real)
The real part of complex number is: 28.0
>>> print("The imaginary part of complex number is:", complex_num3.imag)
The imaginary part of complex number is: 0.0
