# IMMUTABLE: int, float, str, tuple, bool, frozenset
x = "hello"
print(id(x))    # memory address, say 140234
x = x + " world"
print(id(x))    # DIFFERENT address — new object created!

# MUTABLE: list, dict, set
fruits = ["apple", "mango"]
print(id(fruits))   # say 140500
fruits.append("banana")
print(id(fruits))   # SAME address — object modified in place!