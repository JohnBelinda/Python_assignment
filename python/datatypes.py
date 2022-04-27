#datatypes  - int , float, string , boolean , list(array list) , dictionaries(hash map), tuples , set(hash set ,reset)
a=6
b=5
sem = a+b
#print(sem) 

c=1.2
d=20.4

name = 'pan'
designation = 'tester'


#snake casing (used in python ) the variables cannot have white space and
#  special character
# avoid using builtin keywords(ex = new, int , float, )
#  good t have lower case 
# it is case sensitive 
# for variables must use snake casing

is_valid = True 
is_invalid = False



#camel casing (used in java )
isValiduser = True

#intendation is here = space is acting as intendation , accepts the space.

def sum():
    a=10
    b= 20
    print(a+b)
print("era")    
#here intended plays a role - where in era is printed and then the a+b

sum()

#python is dynamically typed language, java is statically typed language

area = 10
print(area)
print(type(area))
area ="10"
print(area)
print(type(area))

#to calculate tax
income = 10000
tax_percentage = 0.2
tax = income*tax_percentage
print(tax)
#operations are performed

#strings
name= 'sam'
#indexing 0,1,2 and also 0,-2,-1, reverse indexing is also possible in python 
first_name= 'antha' # 0 -4 -3 -2 -1

#string supports indexing and slicing
print(name[-1])

#string index is out of range will be got
#print(name[3])
#in terminal error is in which file, in which line and the error
#  exit code gives error -from the python interpriter , 0 as successful and 1 is showing on only error is present .

print(len(first_name))
#this shows the length of the string 

str_alphabets= "abcdefghi"
print(str_alphabets[0:4])
#string[start_idex:stop_index]
print(str_alphabets[:4])
#string takes default start
print(str_alphabets[1:4])
print(str_alphabets[2:])
print(str_alphabets[0:9:2])

#the 2 is the letters it goes forward 
print(str_alphabets[0:-1])

#the string revers can happen as the below way 
print(str_alphabets[::-1])

#string is immutable 
name = "tin"  "tom"
#to change tin to tom
n1 = name[0]+"o"+name[2]
print(n1)

i=10  # i is stored as 10
i="string" #here i takes the value of santhosh now 




