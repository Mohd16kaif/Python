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

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[3:6]) # 3 is start and 6 is end index, end is exlusive
print(nums[:5]) #if start or end not declared, then it considers the first and last element of the list

print(nums[:]) #if both not given, then gives full list