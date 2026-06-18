import math 
import random
import copy

print('''Hello World!
I am grateful''');
print('Hello','\bworld')
name=input("Enter your Name: ")
print("You are",name)
a=10
a="Java"
print(a)
#Types of Data Structures/Collections/Containers
# Dictionary,Set, List, Tuple

#Primitive Data Types int, float, String, Boolean(True|False)
a=None # Type is NoneType, loosely equivalent to not defined 

print(type(a))

#Standalone Functions eg. print() and Type()
#Methods of a class eg. upper() and replace()

#Third Party Libraries: eg. Pandas, TensarFlow, NumPy 

#Functions are independent block of code
#Example:
print("Hello")
type(50)

#Methods are functions belonging to classes
'hello'.upper(); #needs to be printed on console
(50).bit_length();

#############################################################

#Buitin functions for Strings: type() and str()

age=24;
print("Your age is :"+str(24)); #str() converts 24 to a string so that we can concatenate the message

text=''' I am learning Python
Python is Object oriented language
python is must for AI 
'''

print('Count:',text.count('Python'))

date='2026/05/10'
print(date.replace('/','-')) #replace(<oldval>,<newval>)

#f-String: f stands for formatted, lets you easily put variables and expressions directly 
# inside String value
print(f'My name is {name} and I am {age} years old')
print(f'2+3={2+3}')
print(f'{{This is me}}') #To print curly braces in the output

timestamp='01-06-2026 09:20'
print(timestamp.split(' ')) #Split on the basis of space, produces a list of Strings

print('ha'*3)#hahaha

#String Slicing
#Please note that end index is not included
#String can be sliced from right hand side as well, in which case, index starts from -1
str='hello'
print(str[0::1]) # [<start>:<end>:<step>]

" Python".lstrip();
"Python ".rstrip();
" Python ".strip();

print("####ABC##".strip("#"))

print('2026-FEB-10'.startswith('2026'))
print('2026-FEB-10'.endswith('10'))
print('2026-FEB-10'.find('FEB')) #similar to Java's indexOf()
email='prabhjeet.singh92@outlook.com'
print('@' in email)#similar to contains

print("ABC#".isalpha()) # checks if string has only alphabetical characters
print('3.9'.isnumeric()) # check if string is integer

x=5
y=5.7
z=5+2j
print(type(x))
print(type(y))
print(type(z))

x="5"
print(int(x))
a=5
b=7
print(complex(a,b))
print(abs(2-8))

price=35.54678
print(math.floor(price))
print(math.ceil(price))

print(round(price)) 
 
print(round(price,2)) #round to 2 decimal points 

# below two lines produce the same output, they just strip the fractional part and give the 
# integer part as o/p
print(math.trunc(price))
print(int(price))

print(random.random())#random fractional number between 0 and 1
print(random.randint(1,6))#random number between range

x=7.0
print(x.is_integer()) # x is actually an integer

x=7.1
print(x.is_integer())

x=70.0
print(isinstance(x,int))

email=""
phone='123'
name=''
print(any([email,phone,name])) # if any of these has value, return true
print(all([email,phone,name])) # if all have value, return true

# chain comparison
print(1<4<6)

print(2>1 and 1>0)
print(2<1 or 1>0)
print(not 5==5)

name=''
print(not name) # empty string is considered false
print(not 0) # 0 is considered false
print('a' in 'data') 
print(1 in [1,2,3])

a=[1,2,3]
b=[1,2,3]

print(a==b) #compares values

# following expression checks if both variables refer  to the same object, (a and b are 
# different objects) This holds true only for complex objects
print(a is b) # returns false

# for simple data types, for saving memory, single instance is referred 
x=5
y=5
print(x is y) #returns true

email=None
print(email!=None and email!='')
# below is equivalent
print(email is not None and email!='')

score=90
submitted_project=True
if score>=90:
    if submitted_project:
        print('A+')
    else:
       print('A')
elif score>=80:
    print('B')
else:
    print('F')

#inline if, kind of ternary operator equivalent
print('A' if score >= 90 else 'F')

score=20
grade= 'A' if score >=90 else 'B' if score>=80 else 'F'
print(grade)

country='India'

# Available in python 3.10+
match country:
    case 'India'| 'Bharat':
        print('IN')
    case 'Sri Lanka':
        print('SL')
    case _:
        print('Unknown country')


items=(1,2,3,4,5) #it is a tuple
for item in items:
    print(f"Round {item}")

items=[1,2,3,4,5,'A'] #it is a list
for item in items:
    print(f"Round {item}")

items=' Python' 
for item in items:
    print(f"Round {item}")



for item in range(5): # range starts from 0 and iterates from 0 to 4
    print(f"Round {item}")

for item in range(1,5):   # Important: range starts from 1 and iterates from 1 to 4
    print(f"Round {item}")

for item in range(1,10,2):   # Important: range starts from 1 and prints odd numbers b/w 1 to 9
    print(f"Round {item}")   #range(start index, end range,step_count)

for i in (1,2,3):
   if(i%2==0):
    print("Even number found", i)
    break
else:
   print('end')  # this will not execute because break statement executed, if there would have been no break statement, else 
# would have executed after loop completion

letters='Python'
print(list(letters)) #each character becomes a list element

numbers=range(5)
print(list(numbers)) #range becomes a list

matrix=[
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]
print(matrix[2][:2])

#List Unpacking

person=['Maria',29,'Data Engineer','Spain']
name,age,role,country=person
print(name,age)

name,*details,country=person 
# we can have only one * while unpacking unpacking can be done for any type of iterables
print(details)

#we can skip any number of values which are not  required, during unpacking using _
name,_,_,country=person
print(name)
print(country)

# we might have to ignore many values manually using above if we have a long list and we only need first and last values
# we can use the following for such cases.
name,*_,country=person
print(name)
print(country)

numbers=[2,5,800,5]

# built in functions
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))

print(all(numbers)) # will consider 0 as false 
print(all(['','a',''])) # considers empty string as false


print(any(numbers)) # if any value in the list is non zero, it gives true
print(any(['','a',''])) # if any value in the list is non empty, it gives trues

print(numbers.count(5)) # total occurences of value passed
print(numbers.index(5))

print(74 not  in numbers)

list1=[1,2,4]
list2=[1,2,4]
list3=list1

print(list1==list2) #checks meaningful equivalence
print(list1 is list3)# checks reference equivalence

letters=['a','b']
letters.append('c')
letters.insert(3,'d')
print(letters)

letters.append('a')
letters.remove('a') # removes only first occurence of 'a'
print(letters)

letters.pop() # with no argument, removes and returns last value
letters.pop(0) # removes and returns the value at passed index 

letters=['c','b','a']
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)

# if we sort matrix, python sorts based on first element of every list in matrix
matrix.sort();

sorted_copy=sorted(letters,reverse=True); # sorted() creates a sorted copy, while sort() sorts the original list
print("sorted copy:",sorted_copy)

# reversed() creates a  reversed iterator which you pass to list(...) as argument to get reversed list, while reverse() 
# reverses the original list
letters.reverse();
print("Original list reversed:",letters)
reversed_copy=list(reversed(letters)); 
print(reversed_copy)

matrix_copy=matrix.copy() # provides a shallow copy of matrix
matrix_copy=copy.deepcopy(matrix) # provides deep copy of matrix