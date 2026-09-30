a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))
option = int(input("Enter a operation to perform 1.Addition 2.Sub 3.multiplication 4.division"))

if option == 1:
    print(a+b)
elif option == 2:
    print(a-b)
elif option == 3:
    print(a*b)
elif option == 4:
    print(a/b)
else:
    print("Invalid Operation")