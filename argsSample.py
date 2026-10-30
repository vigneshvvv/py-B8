def addN(a,b):
    print(a+b)


def add(*args):
    total = 0

    for num in args:
        total += num
    print(total)


def studentDetails(**kwargs):
    for key, value in kwargs.items():
        print(key, ",", value)



add(10,20)
add(10,20,30)


studentDetails(name ="Arun", age = 22, course = "Python")