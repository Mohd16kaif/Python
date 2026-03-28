#functions in python, they are diff here,  you can assign them to var, pass them as args, return them from other functions, and also you can store them in databases

#here greeting  has a default value
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Arjun"))
print(greet("Ali", "Assalamualaikum"))

#In Python, functions are objects - this means you can store them in varaibles

#u are not calling the greet function here, 
#  greet   # function itself
#  greet()  function call

#so what does this line mean ? it means the say_hi variable will refer to the same function as greet

say_hi = greet

#now you are calling the function, this line is same as greet("Ram")
say_hi("Ram")

#pass function as an argument
def apply(func, value):
    return func(value)

#example
apply(str.upper, "hello")

def nothing(): pass
print(nothing())

#python always returns something - None if no return statement
def nothing(): pass
print(nothing())


#using multiple return values- actually returns a tuple
def minimax(lst):
    return min(lst), max(lst)

lo, hi = minimax([24, 3, 5, 6, 7, 77])
print(lo, hi)

#LEGB rule in python - thhis is how python searches for variables
#B means built in like print, len etc.

x = "global" #defined at the top level of the file

def outer():
    x = "enclosing"
    def inner():
        x = "local" 
        print(x) #local : inside a current function
    inner()
    print(x) #enclosing : inside outer function, nested

outer()
print(x) #global

#global and non - local

count = 0 #created a globla variable here
def increment(): #increment function defined, not executed yet

#what does global mean here ? when i use count, i mean the global variable, not a local one, because in python every var that is used in any func is assumed a local thats why

#without "global count" python thinks count is a local variable, if not used global - UnboundLocalError

    global count
    count +=1

#first understand structure here, we have nested functions here, outer and inner, so there are 2 scopes here x = 10 and inner() tries to use x

def outer():
    x = 10
    def inner():

        #understanding nonlocal here : it means that x here is not local (its not the variable of the inner function inner()). go find the nearest outer enclosing function (outer() that uses that one)
        nonlocal x
        x += 1
    inner()
    print(x)        
outer()

#overall : WE USE "nonlocal" bcoz of pythons this rule "if u assign a var inside any function, pytHon assumes its LOCAL"

#  *args and **kwargs - star args and keyword args or double start key word args

# they are just special syntax to accept flexible inputs in functions, like varargs in java

# *args - extra positional arguments


def add(*args):

    #sum is a prebuilt function here
    return sum(args)
#what happens here is *args collect all the extra arguments into a tuple

print(add(1, 2, 3, 4, 5)) #output : 15 


# **kwargs - they called all the finction argument and store them  into a dict - dictionary

def show(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}, {v}")
print(show(name="Arn", age="34"))     

# combining order - order : normal : *args, **kwargs

def everything(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

everything(1, 2, 3, 4, 5, 6, x = 10)

# *nums unpacks the list into separate arguments (1, 2, 3), so they can be passed individually to the function.

nums = [1, 2, 3]
print(add(*nums))

#  **config unpacks the dict into keyword arguments (a=2, b=4, c=6

config = {"a":2, "b":4, "c":6}
def f(a, b, c) : return a + b + c
print(f(**config))

# lambda functions - a small anonymous function - single expression,  implicit return

# A lambda is just a small, one-line function without a name

#normal func vs lambda func

def square(x):
    return x * 2

square = lambda x: x*2

#core rules for lambda functions

# 1. one expression only
# eg : lambda x: x + 1 ALLOWED
# eg : lambda x: x + 1, x + 3  NOT ALLOWED

# 2. No return keyword, it automatically returns the result
# eg : lambda x: x * 2 returns automatically

# 3. can take multiple inputs 
# eg : lambda x, y: x * y


# HOW TO READ A LAMBDA, THIS IS THE KEY

# square = lambda x: x*2 "A FUNCTION THAT TAKES X AND RETURNS X^2"

add = lambda p,q,r: p + q + r
print(add(10, 20, 0))

# most common use

names = ["Rahul", "Priya", "Arjun", "Lal"]

#if we use sort() here, it will short it alphabetically like arjun, lal....
# but we are sorting it using key and by length like lal - 3 so - lal, rahul...

# Most common use — sort key
names = ["Arjun", "Priya", "Ravi", "Meena"]
names.sort(key=lambda name: len(name))
print(names)

people = [{"name": "Arjun", "age": 25}, {"name": "Priya", "age": 22}]
people.sort(key=lambda p: p["age"])
print(people)

# with filter and map

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x:x%2 == 0, nums))
doubled = list(map(lambda x: x * 2, nums ))

print(evens)
print(doubled)

# list comprehesnsions - A short way to create lists using a single line

# normal way vs list comprehensions

squares = []
for x in range(6): # this means 0 to 5
    squares.append(x ** 2)

squares = [x ** 2 for x in range(6)] # same thing but cleaner
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

upper = [i.upper() for i in ["hello", "world"]]
print(upper)

# nested

matrix = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
print(matrix)
flatten = [num for row in matrix for num in row] # For each row in matrix, and for each number in that row, collect the number”
print(flatten)


# ternary insidw

lables = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(lables)

#dict 
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)


# generator expression - its was concise way to create a iterator that produces values lazily - one at a time, instead of storing all values in memory at once.

#it looks similar to list iterator but instead of [], it uses () paranthesis. the key idea is that a generator expression does not compute results immediately, it generates each value when needed, which makes it memory efficient and suitable for large datasets

gen = [x**2 for x in range (10)] #allocates 1000 items

print(gen)

for i in gen:
    print(i)
