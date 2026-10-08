t= (100,200,400,300,400)
print(t[0])
print(t[-1])
# t[1] = 150

print(t[1:3])
print(len(t))

print(300 in t)

print(t.count(400))

print(t.index(100))

t1 = (10,20,30,40)
t2 = (40,50,60,70)

t3 = t1+t2
print(t3)

for i in t:
    print(i)

print(min(t))
print(max(t))
print(sum(t))

t4 = (20,10,30,15,40)
x = sorted(t4)

print(x)
names = ("f", "i")
print(sum(names))

person = ("Arun", 25, "Developer")
# print(sum(person))

name, age, role = person

print(name)
print(age)
print(role)

t5 = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

print(t5[1][1])

x = list(x)
x[1] = 17
x = tuple(x)

print(x)