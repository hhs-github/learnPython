# -*- coding: utf-8 -*-
"""
Python Data types 
1. none type 
2. numeric type
    2.1 int
    2.2 float
    2.3 complex
3. sequence type 
    3.1 str
    3.2 bytes
    3.3 bytearray
    3.4 list
    3.5 tuple 
    3.6 range 
4. sets
5. mappings 
"""


#a=10
#print("value of a is =" , a)
#b=300.4
#print("value of b is =" , b)
#c= a+b
#print("Sum =" , c)


# function to add two numbers 

def addNum(x,y) :
    """ Function to add two given input numbers """
    print("sum of given two number is ", x+y)


addNum(3,4)
addNum(3+2j , 5+1.9j)

# program to convert to decimals 
# octal value 
n1 = 0o34
#binary value
n2 = 0b1100110
#hexadecimal value
n3 = 0x2d55

#convert octal to decimal
n= int(n1)
print(n)
#convert binary to decimal
n=int(n2)
print(n)
#convert hexa to decimal
n=int(n3)
print(n)

###########################################################################

# converting string to differnt types 

s1 = '34'
s2='1100110'
s3='2d55'

#convert s1 - octal to decimal 
s=int(s1,8)
print(s)

# convert s2 - binary to decimal 
s=int(s2,2)
print(s)

#convert s3 - hexa to decimal
s=int(s3,16)
print(s)

############################################################################

# sequnce data types 
# str - group of characters enclosed by single or double quotes 

s1 = "This is a string datatype"
print(s1)
# triple double quotes can span a string with multiple lines and is useful to embed a string with quotes
s2 = """ this is string with multiple lines
testing str 'data type' with tripple quotes"""
print(s2)

# strings can be sliced based on the charcter position 
print(s1)
print(s1[0])
print(s1[1])
print(s1[1:10])
print(s1[11:])
print(s1[-1])
print(s1[:-1])

##########################################################################
#byte data type 
# byte data type represents a group of byte number ( 0 to 255) in the form a array 
# it does not support negative number
# can not modified or edited

l1 = [0, 1, 2, 30, 40, 100, 200, 255]
b1= bytes(l1)
print(b1)
s= b1.decode('utf16')
print(type(s))
print(s)

print(b1[0])
for i in b1: print(i)

b11 = b"this is byte string "
print(b11)

b12 = b""" this is a multiline 
byte string 
"""
print(b12)

# creating from iterable list
b13 = bytes('Python,java,golang','utf8')
print(b13)


#bytearray 
# similar to byte data type 
# bytearray can be modified 

el = [10,20,30,40,100,200,255]
b2 = bytearray(el)
for i in b2 : print(i)
# modifying element in byte array 
b2[1] = 21
b2[4] = 41
print('printing the byte array again')
for i in b2 : print(i)

##############################################################################

# List Datatype 
# list is similar to array 
# array can hold only one type of element list can hold different type of elements 
# list can be modified 
list =[1,2,'abd',"ww2w"]
print(list)

############################################################################
#Tuple Dataype
# group of elements of different types 
# can not be modified 
# slicing of tuple is allowled 

tup =(1,2,'abe',"w2etr3")
print( tup)
#tup[0] = 22
print(tup[1:3])
print(tup*2)
print(tup[-3])

##############################################################################

# Range Data type 
# sequence of numbers 
# numbers are not modifiable 
# used of iterating the for loop for number of times 

x = range(10)
print(x)

for i in x : 
    print(i)
    
r = range(10,100,5)
for i in r : 
    print(i)
    
# range can used to create a list object 
l1 = list(range(0,20))
print(l1)

#############################################################################

# Set datatypes
#unordered collection of elements 
# elements may not appear in the same order as entered 
# set does not allow duplicates. 
# two types of set 
#   1. set datatype
#   2. frozen datatype 

s1={1,2,3,4,5,6,7,8}
print(s1)

# Create Set using a inbuilt method
# set removes duplicate characters in the given string
s2 = set("this is a set")
print(s2)

# list can be converted as set 

s3 = set(list(range(1,100,5)))
print(s3)

# add an element to the set
# add method can add only one element  
s3.add(10)
print(s3)

# add mulitple elements to set using update method 
# update() method does union operation with given elements and the set itself
s3.update([20,30,40])

# remove() method removes and element in the set 

s3.remove(11)
print(s3)

#############################################################################3
#Frozenset datatype 
# this is similar to set except that elements can not be modified 
# update() , remove() method does not work in frozen set 

fs=frozenset(s3)
print(fs)

#fs.update([50,60])  update() not available for frozen set .

#############################################################################

#Mapping Datatypes 
# a map = key value pair (key:value)

d={100:'Arun',101:'Bala',103:'Chitra',104:'Danny',105:'Eshan'}
print(d)

d[100] = 'Arvind'
d[103]='Chandu'
print(d)

#########################################################################

# Escape characters in the string 

# New line continuatino
s2 ='Escape characters escape the normal meaning and are useful \ to perform a different task'
print(s2)

#to print single \
s2 ='Escape characters escape the normal meaning and are useful \\ to perform a different task'
print(s2)

# to include '
s2 ='Escape characters escape the normal meaning and are useful \'to perform a different task\''
print(s2)

# to have a backspace
s2 ='Escape characters escape the normal meaning and are useful\b to perform a different task'
print(s2)

# enter 
s2 ='Escape characters escape the normal meaning and are useful \r to perform a different task'
print(s2)

# horizontal tab
s2 ='Escape characters escape the normal meaning and are useful \t to perform a different task'
print(s2)

# vertical tab
s2 ='Escape characters escape the normal meaning and are useful \v to perform a different task'
print(s2)

# new line 
s2 ='Escape characters escape the normal meaning and are useful \n to perform a different task'
print(s2)

########################################################################

# Key Words
and 
del 
from 
nonlocal 
try  
as 
elif 
global 
not 
while  
assert 
else 
if 
or 
with  
break 
except 
import 
pass 
yield  
class 
exec 
in 
print 
False  
continue 
finally 
is 
raise 
True  
def 
for 
lambda 
return

###########################################################################

# Naming Conventions 

Package = all lower case with _ between words 
Modules  = all lower case with _ between words 
Classes = Each word in the class should start with Caps , when a class represents an exception then class should end with keyword "error" 
Global Variable or Module variables = all lower case with _ between words 
instance variable = all lower case with _ between words , Non public instance variables start with _
Functions = all lower case with _ between words
Methods = all lower case with _between words
Method arguments =  in case of instance method first argument name should 'self' in case of class method 'cls'
Constants = all uppercase with _ between Words
Non Accessible entities = always start with __

