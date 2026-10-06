for i in range(1,5):
    print(i)

for i in range(0,10,2):
    print(i)

numbers = [10,20,30,40,50,60,70]


for i in range(len(numbers)):
    print(numbers[i])

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])


for num in numbers:
    if num == 30:
        print("number present")
        break
        # continue

    print(num)