Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> score = int(input("enter the score: "))
enter the score: 60
>>> if score>=90:
...     print("the grade is A")
... elif(score<=89 and score >=80):
...     print("the grade is B")
... elif(score<=79 and score>=70):
...     print(*"the grade is C")
... elif(score<=69 and score>=60):
...     print(*"the grade is D")
... else:
...     print("the grade is F")
... 
...     
t h e   g r a d e   i s   D
>>> 
>>> 
>>> 
>>> 
>>> print(" the first 10 natural numbers are: ")
 the first 10 natural numbers are: 
>>> for i in range(1, 11):
...     print(i)
... 
...     
1
2
3
4
5
6
7
8
9
10
>>> 
>>> 
>>> 
>>> 
>>> digit = int(input("enter the number: "))
enter the number: 5
>>> string = str(digit)
>>> count = len(sting)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    count = len(sting)
NameError: name 'sting' is not defined. Did you mean: 'string'?
>>> count = len(string)
>>> print("the number of digits in ", digit, "is:", count)
the number of digits in  5 is: 1
