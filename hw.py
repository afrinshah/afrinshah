Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> marks=[22,34,54,35,55]
>>> print(marks)
[22, 34, 54, 35, 55]
>>> marks.insert(1,32)
>>> print(marks)
[22, 32, 34, 54, 35, 55]
>>> marks.sort()
>>> print(marks)
[22, 32, 34, 35, 54, 55]
>>> marks.remove(22)
>>> print(marks)
[32, 34, 35, 54, 55]
>>> print(marks[:2])
[32, 34]
