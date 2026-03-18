x = 5
print(x)
x = "hello"
print(x)
x = [1,2]
print(x)

#mutable - in place modification possible, i.e at the same memory address

age = 20

if age >= 19:
    print("Adult") #inside the block
    print("Can Vote!") #still inside the block
print("Always runs") #coz, outside the block


print(type(x))
print(isinstance(x, list))

#immutable : int, float, str,  tuple, bool, frozenset

x = "hello"
print(id(x)) #gives memory address eg 2544445599552

x = x  + "world"
print(id(x)) #differn address, coz new obj created eg 2544445685296


#mutable : list, dict, set
fruits = ["apple", "mango"]
print(id(fruits)) #same address after modification that means mutable - in place
fruits.append("banana")
print(id(fruits))

lst = [1, 2, 3]
def add_item(lst):
    lst.append(99)
    print(lst)
    print(id(lst))

add_item(lst)    


def change_num(n):
    n = n + 1 #creates a new int, original unchanged, coz int is immutable
    print(n)
    print(id(n))

n = 12
print(id(n))
change_num(n)        

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# == checks value equality and is checks identity - menmory address
print(a == b) #true
print(b == c) #true
print(a is b) #false - in diff places in memory
print(a is c) # true

#tricky - python caches small intergers from -5 to 256 for performance
x = 256
y = 256
print(x is y)

n = 257
m = 257
print(n is m)

#python also interns short strings, so TRUE, it should be false coz str is immuntable and s1 and s2 should have created 2 diff str at 2 diff places
s1 = "hello"
s2 = "hello"
print(s1 is s2)


a = [1, 2, 3]
b = a
# now a and b points to the same list, and hence list is mutable and changing b, a will also change
b.append(4)
print(a)

#true copy
b = a.copy() #shallow copy - independent list
b.append(99)
print(a) # a is not unaffected - [1, 2, 3 4]
print(b)