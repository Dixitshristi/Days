#operation 

#1
#Returns the total number of elements in a tuple

a = (2,4,6,8,2,45,67,34,100,1234,2,2,2)
print(len(a)) 

#2
#Concatenation (+)
#Combines two or more tuples into a single tuple.

ab = (2,4)
ba = (4,2)
print(ab+ba)

#3
#Repetition (*)
#Repeats tuple elements a specified number of times.
print(a*2)

#4
'''Membership (in, not in)
Checks whether an element exists in a tuple.'''

print(2 in a)

#5
'''Slicing
Slicing is used to get a part (subset) of a tuple.'''
print(a[1:3])

#6
#Accessing Elements
#Accessing means getting elements from a tuple using index numbers.
print(a[0])

#7
#Iteration
#Looping through each element of a tuple.
t = ('a', 'b', 'c')
for i in t:
    print(i)

#8 
#Tuple Unpacking
#Assigning tuple values to multiple variables at once.
t = (100, 200)
a, b = t
print(a, b)

