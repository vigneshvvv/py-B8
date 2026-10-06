numbers = [10,20,30,40,50]
data = [1, "Arjun", True, 30.2]

print(numbers[4])
print(numbers[0])

numbers[1] = 15
print(numbers)

print(len(numbers))
print(numbers[len(numbers)-1])
print(numbers[-1])

numbers.append(60)
print(numbers)

numbers.insert(2, 20)
print(numbers)

print(numbers.index(30))

numbers.remove(15)
print(numbers)

numbers.reverse()
print(numbers)

num = [12,22,11,10,30]
num.sort()
print(num)

num.pop()
print(num)

del num[1]
print(num)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

print(10 in num)
print(20 not in num)

print(a[1:3])

numbers1 = list()
numbers2 = []

numbers.clear()