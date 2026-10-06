numbers = {10,20,30,40,30}
print(numbers)

s = set()

numbers.add(50)
print(numbers)

numbers.update([60,70,80])
print(numbers)

# numbers.remove(90)
# print(numbers)

# numbers.discard(90)
# print(numbers)

# numbers.clear()

# print(len(numbers))

# print(20 in numbers)

a = {2,3,4}
b = {4,5,6}

# print(a|b)
# print(a.union(b))

# print(a.intersection(b))

# print(a.difference(b))

# print(a.symmetric_difference(b))

a=[100,102,102,104,103,104]
a = set(a)
print(a)
a = list(a)
print(a)