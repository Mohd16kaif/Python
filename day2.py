#list - a list is an ordered and mutable sequence

fruits = ["apple", "banana", "orange", "apple", "banana"]

print(fruits.sort())
print(sorted(fruits))
#indexing - 0 based, -1 will print the last element
print(fruits[-3])

#mutating
fruits[0] = "grapes"
print(fruits[0])
del fruits[0]
print(fruits)

print(len(fruits))
print(fruits.count("apple"))

#slicing - it works on any sequence - list, tuple, strings etc

#basic - start:stop

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[3:6]) # 3 is start and 6 is end index, end is exlusive
print(nums[:5]) #if start or end not declared, then it considers the first and last element of the list

print(nums[:]) #if both not given, then gives full list

#with step - [start:stop:step]

print(nums[::2])  # [0, 2, 4, 6, 8] every other element

nums[1::2] #start from 1 to the last, with every other ele
nums[::-1] #start from first to last, but -1 is for reverse
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  reversed

#negative index

nums[-3:] # -3 means start from the last 3rd, and nothing at stop means go till the end, so   [7, 8, 9] last 3

print(nums[:-3]) #start from first to the last 3rd

#strings works indetically
s = "hello world"

print(s[::2])
s[6:] #world
s[::-1] # dlrow olleh

# slicing always returns  a new object - its a shallow copy

a = [1, 2, 3]
b = a[:]
b.append(99)
print(a) #[1, 2, 3] - we can see 'a' is unaffected here
print(b) #[1, 2, 3, 99]

#tuples - ordered but immutable sequence, its like a locked list

point = (12, 44, 99)
person = ('arjun', 23, 'delhi')

#indexing - same as list
point[0] # 12
point[-1] #44

#unpacking - that here tuples shine
x, y, z = point
name, age, city = person
print(x, y, z)

#swap variables - python trick

a, b = 10, 20
a, b = b, a #swapping done, no temp var needed
print(a, b)

#single element tuple - comma is required

t = (34, ) #this is a tuple
t = (3) # this is just an int, the paranthesis are redundant

#tuple methods - only 2 
t = (2, 4, 6, 8, 10)
t.count(2) # how many times '2' has appeared
t.index(3) # index of  first occurance of '3'